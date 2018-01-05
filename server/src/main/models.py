""" This file contain model of website """
from django.db import models

# Create your models here.

class Car(models.Model):
    """ This car Model"""
    car_id = models.CharField(max_length=20, unique=True, primary_key=True)
    car_password = models.CharField(max_length=150)
    car_type = models.CharField(max_length=20, default="normal")

    def __str__(self):
        return str(self.car_id)

class Workshop(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False)
    venue = models.CharField(max_length=50, null=False)
    logo_url = models.CharField(max_length=200, null=False, default="https://")
    description = models.TextField(null=False)
    reg_start_date = models.DateField(null=True) 
    reg_end_date = models.DateField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    reg_status = models.BooleanField(default=False)
    price = models.DecimalField(null=False, default=0.0, max_digits=8, decimal_places=3)
    team_limit = models.IntegerField(default=1)
    status = models.CharField(max_length=60, default="Comming Soon..")

    def __str__(self):
        return str(self.name)
