from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework import permissions
from .permissions import OwnerPermission, SelfPermission

from core.models import TodoItem
from core.serializers import TodoItemSerializer, UserSerializer


class TodoItemViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated,
                          OwnerPermission]
    serializer_class = TodoItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return TodoItem.objects.filter(owner=self.request.user)


class UserViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin):

    permission_classes = [SelfPermission]

    serializer_class = UserSerializer
    queryset = User.objects.all()
