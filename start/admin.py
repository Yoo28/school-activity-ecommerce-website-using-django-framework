from django.contrib import admin
from start.customer import Customer
from start.product import Product
from start.Orders import Order


admin.site.site_header = 'Django Admin Panel'  


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
