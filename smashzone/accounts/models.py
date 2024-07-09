from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPES = [
        ('admin', 'Admin'),
        ('seller', 'Seller'),
        ('player', 'Player'),
        ('organizer', 'Organizer'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPES)