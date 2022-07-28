from django.shortcuts import render, redirect
from django.views.generic import (ListView, DetailView,
                                DeleteView,CreateView, UpdateView,
                                )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .models import Project


# Create your views here.

class ProjectListView(LoginRequiredMixin,ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 10
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProjectListView,self).get_context_data(*args, **kwargs)
        context['total_projects'] = Project.objects.all().count()
        return context
    
class ProjectAdminListView(LoginRequiredMixin,ListView):
    model = Project
    template_name = 'projects/project_admin.html'
    context_object_name = 'projects'
    paginate_by = 10
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProjectAdminListView,self).get_context_data(*args, **kwargs)
        context['total_projects'] = Project.objects.all().count()
        return context
        
class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project

class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Project
    template_name ='project_update.html'
    
class ProjectDetailView(LoginRequiredMixin,DetailView):
    model = Project 
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'
    
class ProjectAdminDetailView(LoginRequiredMixin,DetailView):
    model = Project
    template_name = 'projects/project_admin_detail.html'
    context_object_name = 'project'
    
class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('projects:project-admin')
    
    
    
    
    
    
    