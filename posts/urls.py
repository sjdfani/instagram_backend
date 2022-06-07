from django.urls import path
from .views import CreatePost, ListPost, RetrieveUpdateDestroyPost, CommentStatusPost, ExplorerPosts

app_name = 'posts'

urlpatterns = [
    path('create/', CreatePost.as_view()),
    path('list/account=<int:pk>/', ListPost.as_view()),
    path('list/post=<int:pk>/', RetrieveUpdateDestroyPost.as_view()),
    path('comment-status/', CommentStatusPost.as_view()),
    path('explorer/', ExplorerPosts.as_view()),
]
