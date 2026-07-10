from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_customers, name='get_customers'),
    path('add/', views.add_customer, name='add_customer'),
    path('update/<int:id>/', views.update_customer, name='update_customer'),
    path('delete/<int:id>/', views.delete_customer, name='delete_customer'),
]
