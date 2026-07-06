from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
        widgets = {
            'emp_id' : forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder': 'Emp id'
            }),
            'emp_name' : forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Emp Name'
                
            }),
            'emp_email' : forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Emp Email'
            }),
            'emp_address' : forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Emp Address'
            })
            
        }