from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_restaurants, name='get_restaurants'),
    path('add/', views.add_restaurant, name='add_restaurant'),
    path('update/<int:id>/', views.update_restaurant, name='update_restaurant'),
    path('delete/<int:id>/', views.delete_restaurant, name='delete_restaurant'),
]
