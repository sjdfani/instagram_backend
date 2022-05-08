from django.urls import path
from .views import Register

app_name = 'users'

urlpatterns = [
    path('register/', Register.as_view()),
]
