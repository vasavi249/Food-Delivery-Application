import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fooddelivery.settings')
django.setup()

from customers.models import Customer
from restaurants.models import Restaurant
from foods.models import Food
from cart.models import Cart
from orders.models import Order

def populate():
    print("Clearing old data...")
    Customer.objects.all().delete()
    Restaurant.objects.all().delete()
    Food.objects.all().delete()
    Cart.objects.all().delete()
    Order.objects.all().delete()

    print("Adding Customers...")
    Customer.objects.create(full_name="Rahul Sharma", email="rahul@gmail.com", phone="9876543210", address="KPHB Colony", city="Hyderabad")
    Customer.objects.create(full_name="Sneha Reddy", email="sneha@gmail.com", phone="9988776655", address="Banjara Hills", city="Hyderabad")

    print("Adding Restaurants...")
    r1 = Restaurant.objects.create(
        restaurant_name="Spicy Kitchen", owner_name="Kiran Kumar", location="Hyderabad", cuisine="South Indian", rating=4.8,
        image_url="https://images.unsplash.com/photo-1552566626-52f8b828add9?auto=format&fit=crop&w=600&q=80"
    )
    r2 = Restaurant.objects.create(
        restaurant_name="Pizza Palace", owner_name="Luigi Mario", location="Mumbai", cuisine="Italian", rating=4.5,
        image_url="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=600&q=80"
    )
    r3 = Restaurant.objects.create(
        restaurant_name="Burger Joint", owner_name="Bob Belcher", location="Delhi", cuisine="American", rating=4.2,
        image_url="https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80"
    )
    r4 = Restaurant.objects.create(
        restaurant_name="Sushi Zen", owner_name="Kenji Sato", location="Bangalore", cuisine="Japanese", rating=4.9,
        image_url="https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=600&q=80"
    )
    r5 = Restaurant.objects.create(
        restaurant_name="Taco Fiesta", owner_name="Maria Garcia", location="Pune", cuisine="Mexican", rating=4.4,
        image_url="https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=600&q=80"
    )
    r6 = Restaurant.objects.create(
        restaurant_name="The French Bakery", owner_name="Pierre Dubois", location="Chennai", cuisine="Desserts", rating=4.7,
        image_url="https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=600&q=80"
    )
    r7 = Restaurant.objects.create(
        restaurant_name="Healthy Bites", owner_name="Sarah Connor", location="Gurgaon", cuisine="Healthy", rating=4.6,
        image_url="https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=600&q=80"
    )
    r8 = Restaurant.objects.create(
        restaurant_name="Curry House", owner_name="Amit Patel", location="Kolkata", cuisine="North Indian", rating=4.5,
        image_url="https://images.unsplash.com/photo-1517244683847-7456b63c5969?auto=format&fit=crop&w=600&q=80"
    )

    print("Adding Food Menu...")
    # Spicy Kitchen
    Food.objects.create(restaurant_name="Spicy Kitchen", food_name="Chicken Dum Biryani", category="Main Course", price=299, availability="Available", image_url="https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=600&q=80")
    Food.objects.create(restaurant_name="Spicy Kitchen", food_name="Mutton Biryani", category="Main Course", price=399, availability="Available", image_url="https://images.unsplash.com/photo-1631515243349-e0cb75fb8d3a?auto=format&fit=crop&w=600&q=80")
    Food.objects.create(restaurant_name="Spicy Kitchen", food_name="Paneer Butter Masala", category="Vegetarian", price=250, availability="Available", image_url="https://images.unsplash.com/photo-1588166524941-3bf61a9c41db?auto=format&fit=crop&w=600&q=80")
    
    # Pizza Palace
    Food.objects.create(restaurant_name="Pizza Palace", food_name="Margherita Pizza", category="Pizza", price=350, availability="Available", image_url="https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=600&q=80")
    Food.objects.create(restaurant_name="Pizza Palace", food_name="Pepperoni Pizza", category="Pizza", price=450, availability="Available", image_url="https://images.unsplash.com/photo-1628840042765-356cda07504e?auto=format&fit=crop&w=600&q=80")
    Food.objects.create(restaurant_name="Pizza Palace", food_name="Garlic Bread", category="Sides", price=150, availability="Available", image_url="https://images.unsplash.com/photo-1587241321921-91a834d6d191?auto=format&fit=crop&w=600&q=80")

    # Burger Joint
    Food.objects.create(restaurant_name="Burger Joint", food_name="Classic Cheeseburger", category="Burger", price=200, availability="Available", image_url="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80")
    Food.objects.create(restaurant_name="Burger Joint", food_name="Double Patty Burger", category="Burger", price=350, availability="Available", image_url="https://images.unsplash.com/photo-1586190848861-99aa4a171e90?auto=format&fit=crop&w=600&q=80")
    Food.objects.create(restaurant_name="Burger Joint", food_name="French Fries", category="Sides", price=99, availability="Available", image_url="https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=600&q=80")
    Food.objects.create(restaurant_name="Burger Joint", food_name="Chocolate Shake", category="Beverages", price=120, availability="Out of Stock", image_url="https://loremflickr.com/600/400/shake,chocolate")

    # Sushi Zen
    Food.objects.create(restaurant_name="Sushi Zen", food_name="Salmon Sushi Roll", category="Main Course", price=450, availability="Available", image_url="https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=600&q=80")
    Food.objects.create(restaurant_name="Sushi Zen", food_name="Miso Soup", category="Sides", price=150, availability="Available", image_url="https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=600&q=80")

    # Taco Fiesta
    Food.objects.create(restaurant_name="Taco Fiesta", food_name="Spicy Chicken Tacos", category="Main Course", price=220, availability="Available", image_url="https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=600&q=80")
    Food.objects.create(restaurant_name="Taco Fiesta", food_name="Nachos with Guacamole", category="Sides", price=180, availability="Available", image_url="https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?auto=format&fit=crop&w=600&q=80")

    # The French Bakery
    Food.objects.create(restaurant_name="The French Bakery", food_name="Chocolate Croissant", category="Desserts", price=120, availability="Available", image_url="https://loremflickr.com/600/400/croissant")
    Food.objects.create(restaurant_name="The French Bakery", food_name="Macarons Box", category="Desserts", price=300, availability="Available", image_url="https://images.unsplash.com/photo-1569864358642-9d1684040f43?auto=format&fit=crop&w=600&q=80")

    # Healthy Bites
    Food.objects.create(restaurant_name="Healthy Bites", food_name="Avocado Quinoa Salad", category="Vegetarian", price=280, availability="Available", image_url="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=600&q=80")
    Food.objects.create(restaurant_name="Healthy Bites", food_name="Green Detox Smoothie", category="Beverages", price=150, availability="Available", image_url="https://loremflickr.com/600/400/smoothie")

    # Curry House
    Food.objects.create(restaurant_name="Curry House", food_name="Butter Chicken", category="Main Course", price=350, availability="Available", image_url="https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=600&q=80")
    Food.objects.create(restaurant_name="Curry House", food_name="Garlic Naan", category="Sides", price=60, availability="Available", image_url="https://loremflickr.com/600/400/naan")

    print("Adding to Cart...")
    Cart.objects.create(customer_name="Rahul Sharma", food_name="Chicken Dum Biryani", quantity=2, price=299)
    Cart.objects.create(customer_name="Rahul Sharma", food_name="Garlic Bread", quantity=1, price=150)

    print("Adding Order...")
    Order.objects.create(customer_name="Rahul Sharma", restaurant_name="Spicy Kitchen", order_items="Chicken Dum Biryani (x2)", total_amount=598, payment_status="Paid", delivery_status="Out for Delivery")

    print("Sample Data Populated Successfully!")

if __name__ == '__main__':
    populate()
