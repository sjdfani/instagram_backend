from django.urls import path
from .views import CreateFollowing, DestroyFollowing, ListFollowing, DestroyFollower, ListFollower

app_name = 'follows'

urlpatterns = [
    path('following/create/', CreateFollowing.as_view()),
    path('following/destroy/following=<int:pk>/', DestroyFollowing.as_view()),
    path('following/list/account=<int:pk>/', ListFollowing.as_view()),
    path('follower/destroy/follower=<int:pk>/', DestroyFollower.as_view()),
    path('follower/list/account=<int:pk>/', ListFollower.as_view()),
]
