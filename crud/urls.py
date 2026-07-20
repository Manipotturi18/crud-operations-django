from django.urls import path

from crud import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('emp_create/',views.employee_create, name='emp_create'),
    path('emp_list/', views.employee_list, name='emp_list'),
    path('emp_edit/<int:id>/',views.employee_update,name='emp_edit'),
    path('emp_delete/<int:id>/',views.employee_delete,name='emp_delete'),
]