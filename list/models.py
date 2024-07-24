from django.db import models
from pip._vendor.rich.markup import Tag


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=100)
