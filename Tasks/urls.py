from django.urls import path
from .views import TaskList,TaskDestroy,TaskDetailUpdate, TaskCreate

urlpatterns = [
    path('taskcreate/', TaskCreate.as_view()),
    path('tasklist/', TaskList.as_view()),
    path('taskdestroy/', TaskDestroy.as_view()),
    path('taskdetail/<int:pk>/', TaskDetailUpdate.as_view())
]
