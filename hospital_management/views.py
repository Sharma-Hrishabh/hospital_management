from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from . import forms

app_name='main'

def home(request):
    return render(request,'index.html')
    # return HttpResponse('Hello')


def add_doctor(request):
    if request.method=='POST':
        form=forms.AddDoctor(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('doctor added')

    else:
        form=forms.AddDoctor()
    return render(request,'hospital_management/doctor.html',{'form':form})
