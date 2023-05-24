from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Task
from .serializer import TaskSerializer


class TaskCreate(generics.ListCreateAPIView,generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    #
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

#
# class TaskDetailUpdate(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

#
# class TaskDestroy(generics.DestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
