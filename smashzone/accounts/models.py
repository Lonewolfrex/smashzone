from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass  # Add any additional fields or methods here if needed

class Profile(models.Model):
    ROLE_CHOICES = [
        ('Player', 'Player'),
        ('Organizer', 'Organizer'),
        ('Seller', 'Seller'),
        ('Sponsors', 'Sponsors'),
        ('Admin', 'Admin'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    roles = models.CharField(max_length=255, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username
