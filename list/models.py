from django.db import models


class Task(models.Model):
    STATUS_CHOICES = (
        ("done", "DONE"),
        ("not done", "NOT DONE"),
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    status = models.BooleanField(default=False, choices=STATUS_CHOICES)
    tags = models.ManyToManyField("Tag")

    class Meta:
        ordering = ["status"]


class Tag(models.Model):
    name = models.CharField(max_length=100)
