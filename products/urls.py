from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<item_id>/', views.edit_product, name='edit_product'),
    path('delete/<item_id>/', views.delete_product, name='delete_product'),
]
