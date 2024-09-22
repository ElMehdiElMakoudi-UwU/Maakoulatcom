# project_name/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin interface
    path('', include('employees.urls')),  # Include the employees app's URLs
    path('api-auth/', include('rest_framework.urls')),  # This will add login functionality for the browsable API

]
