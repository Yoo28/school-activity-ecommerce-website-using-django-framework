"""
URL configuration for Ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from start.checkout import  checkout

from start.cart import remove_from_cart
from start.cart import add_to_cart
from start.home import shop
from start.cart import cart
from start.home import home, base

from start.login import Login
from start.signup import Signup
from start.views import  default_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),


   path('', default_view, name='default'),

    path('base/', base, name='base'),
    path('home/', home, name='home'),
    path('cart/', cart, name='cart'),
    path('shop/', shop, name='shop'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/', remove_from_cart, name='remove_from_cart'),
    
    
    path('checkout/', checkout, name='checkout'), 
   
    



] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)