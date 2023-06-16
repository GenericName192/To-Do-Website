from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    taskDescription = models.CharField(max_length=100, verbose_name="Task")
    userId = models.ForeignKey(
        User, related_name="tasks",
        on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)