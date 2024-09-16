from django.contrib import admin
from .models import Product

# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity', 'category', 'date_added')
    search_fields = ('name', 'category')
    list_filter = ('category', 'date_added')

