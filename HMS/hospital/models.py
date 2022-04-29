from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.IntegerField()
    special = models.CharField(max_length=30)


class Patient(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.TextField()


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
