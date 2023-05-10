from django.urls import path, include
from .views import UserList,UserDetailUpdate

urlpatterns = [
    path('userlist/', UserList.as_view()),
    path('userdetail/<int:pk>/', UserDetailUpdate.as_view()),

]
