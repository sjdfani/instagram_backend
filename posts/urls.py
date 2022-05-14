from django.urls import path
from .views import CreatePost, ListPost, RetrieveUpdateDestroyPost

app_name = 'posts'

urlpatterns = [
    path('create/', CreatePost.as_view()),
    path('list/', ListPost.as_view()),
    path('list/<int:pk>/', RetrieveUpdateDestroyPost.as_view()),
]
