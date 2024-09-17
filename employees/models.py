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
    
class ListOfProduct(models.Model):
    name = models.CharField(max_length=200)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='product_lists')
    products = models.ManyToManyField(Product, related_name='product_lists')
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.employee.get_full_name()}"