from django.views.generic import ListView
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = "task/task_list.html"
    context_object_name = "tasks"

class ProjectDetailView(TemplateView):
    template_name = 'tasks/project_detail.html'
class ProjectDeleteView(TemplateView):
    template_name = 'tasks/project_confirm_delete.html'
class TaskDeleteView(TemplateView):
    template_name = 'tasks/task_confirm_delete.html'