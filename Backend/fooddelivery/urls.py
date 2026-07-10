from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # App URLs
    path('customers/', include('customers.urls')),
    path('restaurants/', include('restaurants.urls')),
    path('foods/', include('foods.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
]
