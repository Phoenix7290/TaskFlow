"""
URL configuration for taskflow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    
    path("tasks/", TaskListView.as_view(), name="task-list"),  
    path("<int:pk>/", TaskDetailView.as_view(), name="task-detail"), 
    path("create/", TaskCreateView.as_view(), name="task-create"), 
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),  
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    
    # teste estático para front
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
     
]