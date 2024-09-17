from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, ProductViewSet, ListOfProductsViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'list-of-products', ListOfProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]