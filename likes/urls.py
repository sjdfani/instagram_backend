from django.urls import path
from .views import CreateLike, ListLike,RetrieveDestroyLike

app_name = 'likes'

urlpatterns = [
    path('create/', CreateLike.as_view()),
    path('list/post/<int:pk>/', ListLike.as_view()),
    path('list/ret-des/<int:pk>/', RetrieveDestroyLike.as_view()),
]
