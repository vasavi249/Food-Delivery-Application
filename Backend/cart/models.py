from django.db import models

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    food_name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_name} - {self.food_name}"
