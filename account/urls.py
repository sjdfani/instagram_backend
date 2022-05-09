from django.urls import path
from .views import AccountDetails

app_name = 'account'

urlpatterns = [
    path('account-details/',AccountDetails.as_view()),
]
