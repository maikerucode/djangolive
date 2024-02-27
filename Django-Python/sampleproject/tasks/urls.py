from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.taskList, name="home"),
    path("add", views.addTask, name="add"),
    path("clear", views.clearSesh, name="clear"),
    path("edit", views.editTask, name="edit")
]