""" This file contain model of website """
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Workshop(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False)
    venue = models.CharField(max_length=50, null=False)
    logo_url = models.CharField(max_length=200, null=False, default="https://")
    background_url = models.CharField(max_length=200, null=False, default="https://")
    description = models.TextField(null=False)
    short_description = models.CharField(max_length=400, null=False)
    reg_start_date = models.DateField(null=True)
    reg_end_date = models.DateField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    reg_status = models.BooleanField(default=False)
    status = models.CharField(max_length=60, default = "Comming Soon..")
    wall_status = models.BooleanField(default=False)
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


class WorkshopPlan(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    team_limit = models.IntegerField(default=1)
    details = models.CharField(max_length=600, null=False)
    title = models.CharField(max_length = 50, null=False)
    price = models.IntegerField(default=1)

    def __str__(self):
        return str(self.workshop) +"  "+ str(self.title)


class WorkshopFaqs(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    question = models.CharField(max_length=200, null=False)
    answer = models.TextField(null=False)

    def __str__(self):
        return str(self.workshop) +"  Faq"


class Event(models.Model):
    name =  models.CharField(max_length=50, unique=True, null=False)
    description = models.TextField(null=False)
    date = models.DateField(null=True)
    status = models.CharField(max_length=60, default="Comming Soon..")
    img = models.CharField(max_length=200, null=False, default="https://")
    logo = models.CharField(max_length=200, null=False, default="https://")
    offical_link = models.CharField(max_length=200, null=False, default="https://")
    theme_color = models.CharField(max_length=10, default = "#84859d")
    short_description = models.CharField(max_length=400, null=False)

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
    Mechanical = 'Mechanical'
    Innovation = 'Innovation'
    CATEGORY_CHOICES = (
        (Innovation, 'Innovation'),
        (Mechanical, 'Mechanical')
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )

    name = models.CharField(max_length=50, null=False)
    student_no = models.IntegerField(null=False, unique=True)
    year = models.IntegerField(null=False)
    branch = models.CharField(max_length=30, null=False)
    img = models.CharField(max_length=200, null=False, default="https://")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=False, default=Mechanical)
    department = models.CharField(max_length=20, null=False)
    fb_id = models.CharField(max_length=200, null=False, default="https://")
    gender = models.CharField(max_length=1, null=False, choices=GENDER_CHOICES, default='M')
    contact = models.CharField(default="",max_length=20, null=False)

    def __str__(self):
        return str(self.name)


class Organiser(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.workshop) + " " + str(self.member_id)

class EventTeam(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.event) + " " + str(self.member_id)

class ProjectMaterial(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    material_link =  models.CharField(max_length=200, null=False, default="https://")
    material_name =   models.CharField(max_length=100, null=False) 

    def __str__(self):
        return str(self.project) + " " + str(self.material_name)

class PreWorkshopMaterial(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    material_detail = models.TextField(null=False)
    material_link =  models.CharField(max_length=200, default="https://")
    material_name =   models.CharField(max_length=100, null=False)
    material_img =  models.CharField(max_length=200, default="https://")

    def __str__(self):
        return str(self.workshop) + " " + str(self.material_name)

class WorkshopEnrollment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    team_id = models.CharField(max_length=30, null=False, editable=False)
    workshop_id = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=200)
    leader_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leader')
    enroll_date = models.DateField(default=timezone.now, editable=False)
    is_user_local = models.BooleanField(default=True)
    enroll_status = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user_id', 'workshop_id','enroll_status')
    def __str__(self):
        return str(self.workshop_id) + " " + str(self.team_id)

class UserProfile(models.Model):
    user_college = models.CharField(max_length=100, null=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_contact = models.IntegerField(null=False)
    user_address = models.TextField(null=False)
    user_local = models.BooleanField(default=True)




