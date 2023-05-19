from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Users
from .serializers import UserSerializer


class UserList(generics.ListAPIView, generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

