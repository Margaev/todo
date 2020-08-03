from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from core.views import TodoItemViewSet, UserViewSet

router = DefaultRouter()
router.register(r'todo_items', TodoItemViewSet, basename='todo_item')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls

urlpatterns += [
    path('token-auth/', views.obtain_auth_token, name='token-auth')
]
