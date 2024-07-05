from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('addTask', views.createTask, name='add_task'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]
