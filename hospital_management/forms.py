from django import forms
from . import models


class AddDoctor(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ['name','charge']


class AddPatient(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields=['name','doctor']


class AddMedicine(forms.ModelForm):
    class Meta:
        model = models.Medicine
        fields=['name','price']
