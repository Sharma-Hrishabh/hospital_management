from django import forms
from . import models


class AddDoctor(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ['title','body','slug','thumb']
