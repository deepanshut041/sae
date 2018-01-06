""" This file contain model of website """
from django.db import models

# Create your models here.


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
    status = models.CharField(max_length=60, default = "Comming Soon..")
    theme_color = models.CharField(max_length=10, default = "#84859d")

    def __str__(self):
        return str(self.name)

class Project(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False)
    tech = models.CharField(max_length=200, unique=True, null=False)
    details = models.TextField(null=False)
    img = models.CharField(max_length=200, null=False, default="https://")
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class Event(models.Model):
    name =  models.CharField(max_length=50, unique=True, null=False)
    description = models.TextField(null=False)
    date = models.DateField(null=True)
    status = models.CharField(max_length=60, default="Comming Soon..")
    img = models.CharField(max_length=200, null=False, default="https://")
    logo = models.CharField(max_length=200, null=False, default="https://")
    offical_link = models.CharField(max_length=200, null=False, default="https://")
    theme_color = models.CharField(max_length=10, default = "#84859d")

    def __str__(self):
        return str(self.name)

class Timeline(models.Model):
    date = models.DateField(null=False)
    venue = models.CharField(max_length=50, null=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    achievement = models.CharField(max_length=200, null=False)

    def __str__(self):
        return str(self.event) + str(self.date)


class Member(models.Model):
    Mechanical = 'Me'
    Innovation = 'In'
    CATEGORY_CHOICES = (
        (Innovation, 'Innovation'),
        (Mechanical, 'Mechanical')
    )
    name = models.CharField(max_length=50, null=False)
    student_no = models.IntegerField(null=False, unique=True)
    year = models.IntegerField(null=False)
    branch = models.CharField(max_length=30, null=False)
    img = models.CharField(max_length=200, null=False, default="https://")
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, null=False, default=Mechanical)
    department = models.CharField(max_length=20, null=False)
    fb_id = models.CharField(max_length=200, null=False, default="https://")

    def __str__(self):
        return str(self.name)


class Organiser(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    contact_no = models.IntegerField(null=False)

    def __str__(self):
        return str(self.workshop) + " " + str(self.member_id)
