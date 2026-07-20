from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Employee
from .forms import EmployeeForm, UserRegisterForm, UserLoginForm

# Create your views here.

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('emp_list')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('emp_list')
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('emp_list')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = EmployeeForm()
    return render(request, 'emp_create.html',{'form':form})

@login_required
def employee_list(request):
    employees_list = Employee.objects.all().order_by('emp_id')
    paginator = Paginator(employees_list, 5)  # 5 employees per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'emp_list.html', {'employees': page_obj})

@login_required
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

@login_required
def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('emp_list')

