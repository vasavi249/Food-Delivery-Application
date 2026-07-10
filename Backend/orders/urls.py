from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_orders, name='get_orders'),
    path('add/', views.add_order, name='add_order'),
    path('update/<int:id>/', views.update_order, name='update_order'),
    path('delete/<int:id>/', views.delete_order, name='delete_order'),
]
