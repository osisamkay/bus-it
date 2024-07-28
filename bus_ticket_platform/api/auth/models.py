import uuid
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    company = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    company_logo_url = models.URLField()
    company_slogan = models.CharField(max_length=255)
    user_type = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
