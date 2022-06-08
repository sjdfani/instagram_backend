from django.urls import path
from .views import CreateLike, ListLike,DestroyLike

app_name = 'likes'

urlpatterns = [
    path('create/', CreateLike.as_view()),
    path('list/post=<int:pk>/', ListLike.as_view()),
    path('destroy/account=<int:pk_1>/post=<int:pk_2>/', DestroyLike.as_view()),
]
