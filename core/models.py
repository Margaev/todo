from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    owner = models.ForeignKey('auth.User', related_name='todo_items', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
