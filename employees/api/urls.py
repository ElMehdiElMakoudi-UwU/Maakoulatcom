from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, ProductViewSet, EmployeeProductViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'employee-products', EmployeeProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
