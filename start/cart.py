from decimal import Decimal
from pyexpat.errors import messages
from django.shortcuts import  render
from start.product import Product
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = Decimal(0)

    for product_key, item in cart.items():
        product_key_parts = product_key.split('-')
        product_id = product_key_parts[0]
        selected_size = product_key_parts[1] if len(product_key_parts) > 1 else None

        if not Product.objects.filter(id=product_id).exists():
            
            continue

        product = Product.objects.get(id=product_id)
        subtotal = product.price * item['quantity']

        cart_items.append({
            'product': product,
            'quantity': item['quantity'],
            'subtotal': subtotal,
            'size': selected_size
        })

        total_price += subtotal

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }

    return render(request, 'cart.html', context)


from django.contrib import messages

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    selected_size = request.POST.get('size')  # Assuming the selected size is obtained from the form

    # Retrieve the cart from the session or create a new one if it doesn't exist
    cart = request.session.get('cart', {})

    # Generate a unique key for the product, including the selected size
    product_key = f"{product_id}-{selected_size}"

    # Check if the product is already in the cart
    if product_key in cart:
        # If the product is already in the cart, increment the quantity
        cart[product_key]['quantity'] += 1
    else:
        # If the product is not in the cart, add it with a quantity of 1
        cart[product_key] = {
            'name': product.name,
            'price': float(product.price),  # Convert Decimal to float
            'quantity': 1,
            'size': selected_size  # Add the selected size to the cart
        }

    # Save the updated cart back to the session
    request.session['cart'] = cart

    # Add success message
    messages.success(request, "Product added to cart successfully.")

    return redirect('cart')


from django.contrib import messages

def remove_from_cart(request):
    product_id = request.POST.get('product_id')
    size = request.POST.get('size')

    # Retrieve the cart from the session
    cart = request.session.get('cart', {})

    # Generate the product key for the item to be removed
    product_key = f"{product_id}-{size}"

    # Check if the product is in the cart and remove it
    if product_key in cart:
        if cart[product_key]['quantity'] > 1:
            # If the quantity is more than 1, decrement the quantity
            cart[product_key]['quantity'] -= 1
        else:
            # If the quantity is 1, remove the item from the cart
            del cart[product_key]
        # Add success message
        messages.success(request, "Product removed from cart successfully.")
    else:
        # Add error message if the product is not found in the cart
        messages.error(request, "Product not found in cart.")

    # Save the updated cart back to the session
    request.session['cart'] = cart

    return redirect('cart')
