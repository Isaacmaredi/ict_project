from unicodedata import name
from django.db import models
from django.urls import reverse

from vendors.models import Vendor
from profiles.models import Profile
from contracts.models import Contract

from datetime import datetime, date, timedelta
from django.utils import timezone
from decimal import Decimal

# Create your models here.
PROJECT_STATUS_CHOICES =[
    ('Not Started','Not Started'), 
    ('On track', 'On track'),
    ('Delayed','Delayed'), 
    ('Stopped','Stopped'),
    ('Completed','Completed')
]

PROJECT_ROLES_CHOICES =[
    ('Project Manager','Project Manager'),
    ('Technical Lead','Technical Lead'),
    ('Technical Support','Technical Support'),
    ('User Support','User Suport'),
    ('Business User', 'Business User'),
]

class Deliverable (models.Model):
    name = models.CharField(max_length=300,)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    

class Project(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500, blank=True,null=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    total_cost = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10, 
                                    verbose_name="Total Project Value")
    amount_outstanding = models.DecimalField(default=Decimal('0.0'),blank=True, null=True, decimal_places=2, max_digits=10, 
                                    verbose_name="Amount Outstanding")
    service_provider = models.ForeignKey(Vendor, verbose_name="Service Provider", on_delete=models.DO_NOTHING,
                                        related_name="projects",blank=True, null=True)
    contract = models.ForeignKey(Contract, blank=True, null=True,on_delete=models.DO_NOTHING, related_name="projects")
    status = models.CharField(max_length=150, default= "Not Started", choices=PROJECT_STATUS_CHOICES)
    
    milestone = models.ForeignKey(Deliverable, blank=True,null=True, verbose_name="Milestone",on_delete=models.SET_NULL, related_name="projects")  
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self,**kwargs):
        return reverse('projects:project-admin')

class Team(models.Model):
    name = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='profiles')
    project_role = models.CharField(max_length=150, choices=PROJECT_ROLES_CHOICES, 
                                    verbose_name="Project Role",default='Project Manager')
    project = models.ForeignKey(Project,null=True, blank=True, on_delete=models.DO_NOTHING, related_name="team_members")
    
    def __str__(self):
        return f'{self.name} - {self.project_role}'