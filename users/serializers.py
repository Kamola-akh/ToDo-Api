from rest_framework import serializers
from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','name', 'last_name', 'password', 'email']


        # fields = ['user', 'first_name']