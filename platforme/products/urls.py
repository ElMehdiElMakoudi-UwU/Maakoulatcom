from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.product_list, name='product_list'),  # List products
    path('create/', views.create_product, name='create_product'),  # Create new product
]
