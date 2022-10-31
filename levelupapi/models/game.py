from django.db import models

class Game(models.Model):
    
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='Creator')
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    number_of_players = models.IntegerField(null=True, blank=True)
    skill_level = models.IntegerField(null=True, blank=True)
    game_type = models.ForeignKey("Type", on_delete=models.CASCADE)