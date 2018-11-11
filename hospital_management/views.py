from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from . import forms
from .models import Medicine
from django.core import serializers
import json
from django.forms.models import model_to_dict


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




def add_patient(request):
    if request.method=='POST':
        form=forms.AddPatient(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('patient added')

    else:
        form=forms.AddPatient()
    return render(request,'hospital_management/patient.html',{'form':form})


def add_medicine(request):
    if request.method=='POST':
        form=forms.AddMedicine(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('medicine added')

    else:
        form=forms.AddMedicine()
    return render(request,'hospital_management/medicine.html',{'form':form})



def report(request):
    data = Medicine.objects.all()
    return render(request,'hospital_management/report.html',{'data':data});
