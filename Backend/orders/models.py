from django.db import models

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid')
    ]
    DELIVERY_CHOICES = [
        ('Preparing', 'Preparing'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    ]

    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    restaurant_name = models.CharField(max_length=255)
    order_items = models.TextField() # e.g., JSON string of items
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='Pending')
    delivery_status = models.CharField(max_length=20, choices=DELIVERY_CHOICES, default='Preparing')

    def __str__(self):
        return f"Order {self.order_id} - {self.customer_name}"
