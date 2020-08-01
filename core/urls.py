from rest_framework.routers import DefaultRouter

from core.views import TodoItemViewSet

router = DefaultRouter()
router.register(r'todo_items', TodoItemViewSet, basename='todo_item')

urlpatterns = router.urls
