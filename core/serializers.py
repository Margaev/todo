from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from core.models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = TodoItem
        fields = ['id', 'title', 'text', 'owner', 'created']


class UserSerializer(serializers.ModelSerializer):
    todo_items = TodoItemSerializer(read_only=True, many=True)
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())],
                                     required=True)
    password = serializers.CharField(min_length=8,
                                     required=True,
                                     write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'todo_items']
