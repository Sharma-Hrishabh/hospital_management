from django.db import models

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    charge = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Patient(models.Model):
    patient_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
