from django import forms
from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        
        fields = ('emp_name', 'emp_salary','date_of_joining', 'no_of_leaves','fixed_annual_ctc','monthly_ctc' ,'balance_leaves','image')

        widgets = {
            'emp_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'emp_salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'emp_salary'}),
            'date_of_joining': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'date_of_joining'}),
            'no_of_leaves': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'leaves No.'}),
            # 'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'designation'}),
            # 'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'department'}),
            'fixed_annual_ctc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'fixed_annual_ctc'}),
            'monthly_ctc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'monthly_ctc'}),
            'balance_leaves': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'balance_leaves No.'})
 
        }