from django.db import models
import datetime


today = datetime.date.today()

class Task(models.Model):
    title = models.CharField()
    description = models.TextField()
    start_time = models.DateField(default=today)
    deadline = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title