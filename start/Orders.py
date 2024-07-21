from django.db import models
from start.customer import Customer
from start.product import Product

class Order(models.Model):
    customer_email = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    size = models.CharField(max_length=20, blank=True)
    tracking_number = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return f"Order #{self.id}"

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer_id=customer_id).order_by('-created_at')
