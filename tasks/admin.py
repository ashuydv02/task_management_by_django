from django.contrib import admin
from tasks.models import Task

class AdminTask(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'due_date', 'created_on', 'last_updated']

admin.site.register(Task, AdminTask)
