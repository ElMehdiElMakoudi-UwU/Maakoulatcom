# employees/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import EmployeeViewSet, ProductViewSet, EmployeeProductViewSet

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'employee-products', EmployeeProductViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('api/', include(router.urls)),  # All API routes prefixed with /api/
]
