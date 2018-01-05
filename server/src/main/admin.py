from django.contrib import admin

# Register your models here.
from .models import Car, Workshop


admin.site.register(Car)
admin.site.register(Workshop)
