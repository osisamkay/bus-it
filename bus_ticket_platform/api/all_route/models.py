from django.db import models
import uuid
from django.contrib.auth.models import User


class Route(models.Model):
    TRIP_TYPE_CHOICES = [
        ('one_way_trip', 'One Way Trip'),
        ('round_trip', 'Round Trip'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_point = models.CharField(max_length=255)
    end_point = models.CharField(max_length=255)
    distance = models.FloatField()
    duration = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    trip_type = models.CharField(
        max_length=255, choices=TRIP_TYPE_CHOICES, default='one_way_trip')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
