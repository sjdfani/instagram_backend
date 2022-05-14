from django.urls import path
from .views import CreatePost

app_name = 'posts'

urlpatterns = [
    path('create/',CreatePost.as_view()),
]
