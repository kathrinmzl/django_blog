# This file is where we'll list our blog app-specific URLs.
from . import views
from django.urls import path

urlpatterns = [
    # urlpattern for PostList class-based view named home.
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name = 'post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
]