from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView  # Adicione CreateView e UpdateView
from .models import Task, Project
from django.shortcuts import render

# Project List View
class ProjectListView(ListView):
    model = Project
    template_name = "task/project_list.html"
    context_object_name = "projects"

# Project Create View (optional, but needed for project_list.html links)
class ProjectCreateView(CreateView):
    model = Project
    template_name = "task/project_form.html"
    fields = ["name", "description"]
    success_url = reverse_lazy('project_list')

# Project Update View (optional, but aligns with typical CRUD functionality)
class ProjectUpdateView(UpdateView):
    model = Project
    template_name = "task/project_form.html"
    fields = ["name", "description"]
    success_url = reverse_lazy('project_list')

class TaskListView(ListView):
    model = Task
    template_name = "task/task_list.html"
    context_object_name = "tasks"

class TaskDetailView(DetailView):  # Corrigido: fora da classe ProjectDeleteView
    model = Task
    template_name = "task/task_detail.html"
    context_object_name = "task"

class TaskCreateView(CreateView):
    model = Task
    template_name = "task/task_form.html"
    fields = ["title", "description", "project"]
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = "task/task_form.html"
    fields = ["title", "description", "project"]
    success_url = reverse_lazy('task-list')

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
    success_url = reverse_lazy('project_list')