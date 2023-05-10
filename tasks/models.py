from django.db import models
from users.models import Users


class Task(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField()

    def __str__(self):
        return self.title



