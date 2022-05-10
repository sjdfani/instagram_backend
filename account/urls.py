from django.urls import path
from .views import AccountDetails, UpdateInformation, ChangeLanguage, ChangeProfilePhoto

app_name = 'account'

urlpatterns = [
    path('account-details/', AccountDetails.as_view()),
    path('update-information/', UpdateInformation.as_view()),
    path('change-language/', ChangeLanguage.as_view()),
    path('change-profile-photo/', ChangeProfilePhoto.as_view()),
]
