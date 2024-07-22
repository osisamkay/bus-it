import uuid
from django.db import models
from django.contrib.auth.models import User


class Route(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_point = models.CharField(max_length=255)
    end_point = models.CharField(max_length=255)
    distance = models.FloatField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
