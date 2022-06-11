from django.urls import path
from .views import CreateArchivePost, ListArchivePost, DestroyArchivePost

app_name = 'archives'

urlpatterns = [
    path('create/', CreateArchivePost.as_view()),
    path('list/', ListArchivePost.as_view()),
    path('destroy/account=<int:pk_1>/post=<int:pk_2>/',
         DestroyArchivePost.as_view()),
]
