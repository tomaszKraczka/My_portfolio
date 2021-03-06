"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views
app_name = 'tester_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that show all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]