from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("timeDisplay", views.timeDisplay, name="timeDisplay"),
    path("akira", views.swetch, name="swetch"),
    path("<str:name>", views.introduction, name="introduction")
]