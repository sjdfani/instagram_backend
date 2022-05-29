from django.urls import path
from .views import CreatePost, ListPost, RetrieveUpdateDestroyPost, AnotherListPost, CommentStatusPost

app_name = 'posts'

urlpatterns = [
    path('create/', CreatePost.as_view()),
    path('list/', ListPost.as_view()),
    path('list/<int:pk>/', RetrieveUpdateDestroyPost.as_view()),
    path('list/another-acc/<int:pk>/', AnotherListPost.as_view()),
    path('comment-status/', CommentStatusPost.as_view()),
]
