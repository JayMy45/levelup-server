from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):

    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='host')
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    time = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    attendees = models.ManyToManyField('Gamer', blank=True, through='GamerEvent')


    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value