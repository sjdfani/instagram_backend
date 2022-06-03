from django.urls import path
from .views import CreateFollowing, RetrieveDestroyFollowing, ListFollowing, CreateFollower, RetrieveDestroyFollower, ListFollower

app_name = 'follows'

urlpatterns = [
    path('following/create/', CreateFollowing.as_view()),
    path('following/retrieve-destroy/<int:pk>/',
         RetrieveDestroyFollowing.as_view()),
    path('following/list/account=<int:pk>/', ListFollowing.as_view()),
    path('follower/create/', CreateFollower.as_view()),
    path('follower/retrieve-destroy/<int:pk>/',
         RetrieveDestroyFollower.as_view()),
    path('follower/list/account=<int:pk>/', ListFollower.as_view()),
]
