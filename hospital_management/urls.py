from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

app_name='hospital_management'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home,name="home"),
    url(r'^add/doctor/$',views.add_doctor,name="doctor"),
    url(r'^add/patient/$',views.add_patient,name="patient"),
    url(r'^add/medicine/$',views.add_medicine,name="medicine"),
    url(r'^report/',views.report,name="report"),
    

]
