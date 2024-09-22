from django.db import models
from django.contrib.auth.models import AbstractUser

class Employee(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    hire_date = models.DateField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    category = models.CharField(max_length=100, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Intermediate model for the many-to-many relationship with an additional field 'quantity'
class EmployeeProduct(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('employee', 'product')  # Ensures that an employee can have only one entry per product

    def __str__(self):
        return f'{self.employee} - {self.product} (Quantity: {self.quantity})'
