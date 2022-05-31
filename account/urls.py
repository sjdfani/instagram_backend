from django.urls import path
from .views import AccountDetails, UpdateInformation, ChangeLanguage, ChangeProfilePhoto, SetBirthdate, AnotherAccountDetails, CountPostFollows

app_name = 'account'

urlpatterns = [
    path('account-details/', AccountDetails.as_view()),
    path('account-details/<int:pk>/', AnotherAccountDetails.as_view()),
    path('update-information/', UpdateInformation.as_view()),
    path('change-language/', ChangeLanguage.as_view()),
    path('change-profile-photo/', ChangeProfilePhoto.as_view()),
    path('set-birthdate/', SetBirthdate.as_view()),
    path('count-post-follows/', CountPostFollows.as_view()),
]
