from django.urls import path

from crud import views

urlpatterns = [
    path('emp_create/',views.employee_create, name='emp_create'),
    path('emp_list/', views.employee_list, name='emp_list'),
    path('emp_edit/<int:id>/',views.employee_update,name='emp_edit'),
    path('emp_delete/<int:id>/',views.employee_delete,name='emp_delete'),
]