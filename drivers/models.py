from django.db import models
from teams.models import Team
from django.db.models import ForeignKey

# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    team = ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

def __str__(self):
    return self.name