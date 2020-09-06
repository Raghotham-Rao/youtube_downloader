from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('video', views.video),
    path('music', views.music),
    path('playlist', views.playlist)
]
