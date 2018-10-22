from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import employee
from.forms import myemployeeform


def home(request):

    if request.method=='POST':
        form = myemployeeform(request.POST)
        if form.is_valid():
            form.save(commit=True)
    form=myemployeeform()
    return render(request,'home.html',{'form':form})
def profile(request):
    employees = employee.objects.all()
    return render(request,'profile.html',{'employees':employees})