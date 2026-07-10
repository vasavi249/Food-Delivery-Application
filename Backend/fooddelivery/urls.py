from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "status": "success",
        "message": "Welcome to the Food Delivery API!",
        "endpoints": ["/foods/", "/restaurants/", "/customers/", "/cart/", "/orders/"]
    })

urlpatterns = [
    path('', api_root, name='api_root'),
    path('admin/', admin.site.urls),
    
    # App URLs
    path('customers/', include('customers.urls')),
    path('restaurants/', include('restaurants.urls')),
    path('foods/', include('foods.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
]
