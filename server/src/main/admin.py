from django.contrib import admin

# Register your models here.
from .models import (Workshop, Project, Event, Member, Timeline, Organiser,
 WorkshopPlan, WorkshopFaqs, EventTeam, ProjectMaterial, PreWorkshopMaterial,
WorkshopEnrollment)


admin.site.register(Workshop)
admin.site.register(Project)
admin.site.register(Event)
admin.site.register(Member)
admin.site.register(Timeline)
admin.site.register(Organiser)
admin.site.register(WorkshopPlan)
admin.site.register(WorkshopFaqs)
admin.site.register(EventTeam)
admin.site.register(ProjectMaterial)
admin.site.register(PreWorkshopMaterial)
admin.site.register(WorkshopEnrollment)