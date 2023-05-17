from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=128, default=None)
    email = models.EmailField()
    date_of_birth = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

