from django.http import HttpResponse
from django.shortcuts import render

app_name='main'

def home(request):
    return render(request,'index.html')
    # return HttpResponse('Hello')


def add_patient(request):
    return HttpResponse('patient')
