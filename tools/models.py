from django.db import models
from django.utils import timezone


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=255)
    serial_number = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
