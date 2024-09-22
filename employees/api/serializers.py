from rest_framework import serializers
from ..models import Employee, Product, EmployeeProduct

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'username', 'first_name', 'last_name', 'phone_number', 'job_title', 'date_of_birth', 'hire_date', 'salary']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock_quantity', 'category', 'date_added']

class EmployeeProductSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = EmployeeProduct
        fields = ['employee', 'product', 'quantity']
