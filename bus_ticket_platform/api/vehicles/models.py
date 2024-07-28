from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    plate_number = models.CharField(max_length=255, unique=True)
    company = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
