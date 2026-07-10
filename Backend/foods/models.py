from django.db import models

class Food(models.Model):
    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Out of Stock', 'Out of Stock')
    ]

    food_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=255)
    food_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='Available')
    image_url = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.food_name} - {self.restaurant_name}"
