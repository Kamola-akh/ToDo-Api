from django.urls import path
from .views import TaskCreate

urlpatterns = [
    path('taskcreation/', TaskCreate.as_view()),
    # path('tasklist/', TaskList.as_view()),
    # path('taskdetail/<int:pk>/', TaskDetailUpdate.as_view())
]
