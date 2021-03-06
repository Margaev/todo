from rest_framework.permissions import BasePermission


class OwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        else:
            return False


class SelfPermission(BasePermission):
    message = 'You can get only your account info'

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return request.user == obj
        else:
            return True
