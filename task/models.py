from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class ToDo(models.Model):
    
    TODO_CHOICES = (
        ('E', 'Event'),
        ('T', 'Task'),
        ('A', 'Appointment schedule'),
    )
    
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now())
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=TODO_CHOICES)
    
    def __str__(self):
        return f"{self.title} by {self.user.username}"
