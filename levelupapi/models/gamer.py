from django.db import models
from django.contrib.auth.models import User

from levelupapi.models import gamer_event

class Gamer(models.Model):

    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    events = models.ManyToManyField('Event', blank=True, through='GamerEvent')

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'