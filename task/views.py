from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from .models import Task, Project

class TaskListView(ListView):
    model = Task
    template_name = "task/task_list.html"
    context_object_name = "tasks"

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'task/project_details.html'
    context_object_name = 'project'

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'task/project_confirm_delete.html'
    success_url = reverse_lazy('project-list')