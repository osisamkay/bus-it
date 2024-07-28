from django.db import models
from django.conf import settings
from uuid import uuid4
from ..all_route.models import Route
from django.contrib.auth.models import User


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=255)
    trip_type = models.CharField(max_length=255)
    departure_datetime = models.DateTimeField()
    return_datetime = models.DateTimeField(null=True, blank=True)
    seat_number = models.IntegerField(default=0)
    number_of_seats = models.IntegerField()
    payment_method = models.CharField(max_length=255)
    payment_details = models.TextField()
    special_requests = models.TextField(null=True, blank=True)
    discount_code = models.CharField(max_length=50, null=True, blank=True)
    status = models.BooleanField(max_length=50, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking {self.id} by {self.user.username} for route {self.route.name}"
