from django.test import TestCase
from .models import Task, Project

class ModelTest(TestCase):
    def test_task_creation(self):
        project = Project.objects.create(name="Test Project")
        task = Task.objects.create(title="Test Task", project=project)
        self.assertEqual(task.title, "Test Task")