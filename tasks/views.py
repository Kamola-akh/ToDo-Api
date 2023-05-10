from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializer import TaskSerializer


class TaskCreate(generics.ListCreateAPIView,generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# class TaskList(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

#
# class TaskDetailUpdate(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

#
# class TaskDestroy(generics.DestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
