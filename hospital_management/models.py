from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    patient_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    doctor_id=models.IntegerField()
