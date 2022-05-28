from django.urls import path
from .views import CreateComments

app_name = 'comments'

urlpatterns = [
    path('create/', CreateComments.as_view()),
]
