from datetime import datetime

from django.db import models


class Task(models.Model):
    STATUS_CHOICES = (
        ("done", "DONE"),
        ("not done", "NOT DONE"),
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="not done")
    tags = models.ManyToManyField("Tag")

    class Meta:
        ordering = ["status"]

    def save(self, *args, **kwargs):
        if self.status == "done" and not self.deadline:
            self.deadline = datetime.now()
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
