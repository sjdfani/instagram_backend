from django.urls import path
from .views import CreateFollowing, RetrieveDestroyFollowing, ListFollowing, AnotherListFollowing

app_name = 'follows'

urlpatterns = [
    path('following/create/', CreateFollowing.as_view()),
    path('following/retrieve-destroy/<int:pk>/',
         RetrieveDestroyFollowing.as_view()),
    path('following/list/', ListFollowing.as_view()),
    path('following/list/another-acc/<int:pk>/', AnotherListFollowing.as_view()),
]
