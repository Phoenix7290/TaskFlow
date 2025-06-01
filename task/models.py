from django.db import models
from .models import Task
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class Project(models.Model):
    name = models.CharField(max_length=100)

class Task(models.Model):
    STATUS_CHOICES = [
        ("P", "Pendente"),
        ("C", "Concluída"),
        ("EP", "Em_progresso")
    ]

    title = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)