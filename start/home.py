from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    # Your view logic here
    return render(request, 'home.html')


def base(request):
    # Your view logic here
    return render(request, 'base.html')

from django.shortcuts import redirect
from django.views import View

class LogoutView(View):
    def get(self, request):
        # Clear the session data
        request.session.clear()
        return redirect('home')


from django.shortcuts import render
from start.product import Product

def shop(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'shop.html', context)

