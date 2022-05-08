from django.urls import path
from .views import Register, Login, ChangePassword

app_name = 'users'

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('change-password/', ChangePassword.as_view()),
]
