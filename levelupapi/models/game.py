from django.db import models

class Game(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='Organizer')
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    number_of_players = models.IntegerField(null=True, blank=True, editable=True)
    skill_level = models.IntegerField(null=True, blank=True, editable=True)
    game_type = models.ForeignKey("Type", on_delete=models.CASCADE)