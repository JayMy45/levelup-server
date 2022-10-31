from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):

    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='')
    game = models.ForeignKey("", on_delete=models.CASCADE, related_name='')
    description = models.CharField(max_length=50)
    date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    time = 