"""TODOs app models"""

from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    """A simple TODO model"""
    task = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    done = models.BooleanField(blank=True, default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.task} ({self.user.username})'
