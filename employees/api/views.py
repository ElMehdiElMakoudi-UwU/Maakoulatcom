from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Employee, Product, EmployeeProduct
from .serializers import EmployeeSerializer, ProductSerializer, EmployeeProductSerializer
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

# ViewSet for Employee
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]  # Allow any user to access this view


    # Custom action to get the list of products with quantities for a specific employee
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        employee = self.get_object()
        employee_products = EmployeeProduct.objects.filter(employee=employee)
        serializer = EmployeeProductSerializer(employee_products, many=True)
        return Response(serializer.data)

# ViewSet for Product
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# ViewSet for EmployeeProduct (assigning products to employees with quantities)
class EmployeeProductViewSet(viewsets.ModelViewSet):
    queryset = EmployeeProduct.objects.all()
    serializer_class = EmployeeProductSerializer

    # Overriding create to handle custom behavior for adding a product to an employee
    def create(self, request, *args, **kwargs):
        employee_id = request.data.get('employee')
        product_id = request.data.get('product')
        quantity = request.data.get('quantity')

        employee = get_object_or_404(Employee, id=employee_id)
        product = get_object_or_404(Product, id=product_id)

        employee_product, created = EmployeeProduct.objects.get_or_create(
            employee=employee, product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            # If the record already exists, update the quantity
            employee_product.quantity = quantity
            employee_product.save()

        serializer = EmployeeProductSerializer(employee_product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

from django.views.generic import TemplateView

class CreateEmployeeView(TemplateView):
    template_name = 'create_employee.html'


from django.views.generic import TemplateView

class ProductListView(TemplateView):
    template_name = 'product_list.html'

class CreateProductView(TemplateView):
    template_name = 'create_product.html'
