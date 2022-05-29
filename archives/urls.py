from django.urls import path
from .views import CreateArchivePost, ListArchivePost, RetrieveDestroyArchivePost

app_name = 'archives'

urlpatterns = [
    path('create/', CreateArchivePost.as_view()),
    path('list/', ListArchivePost.as_view()),
    path('list/<int:pk>/', RetrieveDestroyArchivePost.as_view()),
]
