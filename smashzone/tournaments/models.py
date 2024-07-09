# tournaments/models.py

from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tournaments(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    sports = models.ManyToManyField(Sport, related_name='tournaments')  # Ensure this line is present
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
