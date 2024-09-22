from django.contrib import admin
from .models import Employee, Product, EmployeeProduct

# Inline for EmployeeProduct (used in EmployeeAdmin)
class EmployeeProductInline(admin.TabularInline):
    model = EmployeeProduct
    extra = 1  # Number of empty forms to display in the admin panel for adding new rows
    min_num = 1
    max_num = 10
    fields = ['product', 'quantity']
    verbose_name = 'Assigned Product'
    verbose_name_plural = 'Assigned Products'

# Admin for Employee
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'phone_number', 'job_title', 'hire_date', 'salary']
    search_fields = ['first_name', 'last_name', 'phone_number', 'job_title']
    list_filter = ['job_title', 'hire_date']
    inlines = [EmployeeProductInline]  # This allows assigning products with quantities in the Employee detail page

# Admin for Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock_quantity', 'category', 'date_added']
    search_fields = ['name', 'category']
    list_filter = ['category', 'date_added']

# Admin for EmployeeProduct
@admin.register(EmployeeProduct)
class EmployeeProductAdmin(admin.ModelAdmin):
    list_display = ['employee', 'product', 'quantity']
    search_fields = ['employee__first_name', 'employee__last_name', 'product__name']
    list_filter = ['employee', 'product']
    autocomplete_fields = ['employee', 'product']
