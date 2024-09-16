from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'job_title', 'date_of_birth', 'hire_date', 'salary')
    search_fields = ('first_name', 'last_name', 'email', 'job_title')
    list_filter = ('job_title', 'hire_date')
    ordering = ('hire_date',)
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'phone_number')
        }),
        ('Employment Details', {
            'fields': ('job_title', 'date_of_birth', 'hire_date', 'salary')
        }),
    )
