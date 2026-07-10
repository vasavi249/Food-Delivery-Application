from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_foods, name='get_foods'),
    path('add/', views.add_food, name='add_food'),
    path('update/<int:id>/', views.update_food, name='update_food'),
    path('delete/<int:id>/', views.delete_food, name='delete_food'),
]
