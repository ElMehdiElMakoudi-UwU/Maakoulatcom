# project_name/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin interface
    path('', include('employees.urls')),  # Include the employees app's URLs
]
