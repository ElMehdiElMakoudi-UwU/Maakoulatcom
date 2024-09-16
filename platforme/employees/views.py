from django.shortcuts import render, redirect
from .forms import EmployeeForm

def register_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new employee to the database
            return redirect('employee_list')  # Redirect to a list of employees or another page
    else:
        form = EmployeeForm()

    return render(request, 'register_employee.html', {'form': form})

def employee_list(request):
    from .models import Employee
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
