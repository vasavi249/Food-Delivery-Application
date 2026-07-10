from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_cart, name='get_cart'),
    path('add/', views.add_cart, name='add_cart'),
    path('update/<int:id>/', views.update_cart, name='update_cart'),
    path('delete/<int:id>/', views.delete_cart, name='delete_cart'),
]
