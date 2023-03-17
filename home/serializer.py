
from .models import TodoTask
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token

class TaskSerializer(ModelSerializer):
    class Meta:
        model=TodoTask
        fields='__all__'


class UserSerialiser(ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

    

    