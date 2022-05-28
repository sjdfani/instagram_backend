from django.urls import path
from .views import CreateFollowing, RetrieveDestroyFollowing, ListFollowing, AnotherListFollowing, CreateFollower, RetrieveDestroyFollower, ListFollower, AnotherListFollower

app_name = 'follows'

urlpatterns = [
    path('following/create/', CreateFollowing.as_view()),
    path('following/retrieve-destroy/<int:pk>/',
         RetrieveDestroyFollowing.as_view()),
    path('following/list/', ListFollowing.as_view()),
    path('following/list/another-acc/<int:pk>/',
         AnotherListFollowing.as_view()),
    path('follower/create/', CreateFollower.as_view()),
    path('follower/retrieve-destroy/<int:pk>/',
         RetrieveDestroyFollower.as_view()),
    path('follower/list/', ListFollower.as_view()),
    path('follower/list/another-acc/<int:pk>/',
         AnotherListFollower.as_view()),
]
