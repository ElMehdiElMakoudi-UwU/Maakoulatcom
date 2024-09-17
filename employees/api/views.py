from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from ..models import Employee, Product, ListOfProduct
from .serializers import EmployeeSerializer, ProductSerializer, ListOfProductSerializer
from rest_framework.authentication import TokenAuthentication


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

class ListOfProductsViewSet(viewsets.ModelViewSet):
    queryset = ListOfProduct.objects.all()
    serializer_class = ListOfProductSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)

    def list(self, request):
        queryset = self.queryset.filter(employee=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)