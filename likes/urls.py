from django.urls import path
from .views import CreateLike, ListLike,DestroyLike

app_name = 'likes'

urlpatterns = [
    path('create/', CreateLike.as_view()),
    path('list/post=<int:pk>/', ListLike.as_view()),
    path('destroy/post=<int:pk>/', DestroyLike.as_view()),
]
