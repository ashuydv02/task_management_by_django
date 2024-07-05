from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    status = models.CharField(max_length=50)
    due_date = models.DateField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
