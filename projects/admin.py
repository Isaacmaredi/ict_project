from django.contrib import admin
from .models import Team, Deliverable, Project
# Register your models here.

admin.site.register(Team)
admin.site.register(Deliverable)
admin.site.register(Project)