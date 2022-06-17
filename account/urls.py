from django.urls import path
from .views import AccountDetails, UpdateInformation, ChangeLanguage, ChangeProfilePhoto, ListAccountInformation, SuggestionAccount

app_name = 'account'

urlpatterns = [
    path('account-details/<int:pk>/', AccountDetails.as_view()),
    path('update-information/<int:pk>/', UpdateInformation.as_view()),
    path('change-language/', ChangeLanguage.as_view()),
    path('change-profile-photo/', ChangeProfilePhoto.as_view()),
    path('list-account-data/', ListAccountInformation.as_view()),
    path('suggestion-account/', SuggestionAccount.as_view()),
]
