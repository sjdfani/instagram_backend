from django.urls import path
from .views import Register, Login, ChangePassword, ForgetPassword, VerifyForgetPassword, ChangeUsername

app_name = 'users'

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('change-password/', ChangePassword.as_view()),
    path('forget-password/', ForgetPassword.as_view()),
    path('verify-forget-password/', VerifyForgetPassword.as_view()),
    path('change-username/', ChangeUsername.as_view()),
]
