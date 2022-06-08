from django.urls import path
from .views import CreateComments,ListComments

app_name = 'comments'

urlpatterns = [
    path('create/', CreateComments.as_view()),
    path('list/post=<int:pk>/', ListComments.as_view()),
]
