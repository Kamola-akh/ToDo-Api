from django.shortcuts import render
from rest_framework import generics
from .models import Users
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
