from django.contrib import admin

# Register your models here.
from .models import Car, Workshop, Project, Event, Member, Timeline, Organiser


admin.site.register(Car)
admin.site.register(Workshop)
admin.site.register(Project)
admin.site.register(Event)
admin.site.register(Member)
admin.site.register(Timeline)
admin.site.register(Organiser)
