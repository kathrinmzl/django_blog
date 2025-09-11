# This file is where we'll list our blog app-specific URLs.
from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_me, name='about'),
]