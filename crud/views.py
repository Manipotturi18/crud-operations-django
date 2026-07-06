from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = EmployeeForm()
    return render(request, 'emp_create.html',{'form':form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request,'emp_list.html',{'employees':employees})

def employee_update(request,id):
    employee = get_object_or_404(Employee,id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form=EmployeeForm(instance=employee)
    return render(request, 'emp_create.html',{'form':form})

def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('emp_list')
