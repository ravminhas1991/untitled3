from django import forms
from .models  import employee
class myemployeeform (forms.ModelForm):
    class Meta:
        model=employee
        fields = ['First_name', 'Last_name', 'DOB','Phone_Number','Address',]