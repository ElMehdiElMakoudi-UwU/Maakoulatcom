from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),  # Include URLs from the 'products' app
    path('employees/', include('employees.urls')),  # Includes URLs from the employees app
]
