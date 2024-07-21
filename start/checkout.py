from decimal import Decimal
import uuid
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from start.Orders import Customer, Product, Order

def checkout(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
       
        cart = request.session.get('cart', {})
        total_price = Decimal(0)
        order_items = []
        keys_to_delete = []
        tracking_number = None  
        
        for product_key, item in cart.items():
            product_id, selected_size = product_key.split('-')
            
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                continue
            
            subtotal = product.price * item['quantity']
            total_price += subtotal
            
            order_items.append({
                'product': product,
                'quantity': item['quantity'],
                'size': selected_size,
                'subtotal': subtotal
            })
            
           
            tracking_number = str(uuid.uuid4())  
            
          
            order = Order(
                customer_name=customer_name,
                customer_email=customer_email,
                product=product,
                total_price=total_price,
                address=address,
                phone=phone,
                quantity=item['quantity'],
                size=selected_size,
                tracking_number=tracking_number
            )
            order.save()
            
        
            keys_to_delete.append(product_key)
     
        for key in keys_to_delete:
            del cart[key]
        
        request.session['cart'] = cart
        
        context = {
            'order_items': order_items,
            'total_price': total_price,
            'customer_name': customer_name,
            'customer_email': customer_email,
            'phone': phone,
            'address': address,
            'tracking_number': tracking_number
        }
        
        
        receipt_html = render_to_string('receipt.html', context)
        
     
        subject = 'Order Confirmation'
        message = 'Thank you for your order!'
        from_email = 'clbapparelfits@gmail.com'  
        to_email = [customer_email]
        send_mail(subject, message, from_email, to_email, html_message=receipt_html)
        
        return render(request, 'checkout.html', context)
    
    return redirect('cart')  
