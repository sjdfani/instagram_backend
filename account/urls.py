from django.urls import path
from .views import AccountDetails, UpdateInformation

app_name = 'account'

urlpatterns = [
    path('account-details/', AccountDetails.as_view()),
    path('update-information/', UpdateInformation.as_view()),
]
