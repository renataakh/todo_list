from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_task/", views.add_task, name="add_task"),
    path("complete/<int:task_id>", views.completed_task, name='completed_task'),
    path("edit_task/<int:task_id>", views.edit_task, name='edit_task'),
    path("incomplete_tasks/", views.incomplete_tasks, name="incomplete_tasks")
]