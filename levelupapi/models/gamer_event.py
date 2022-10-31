from django.db import models

class GamerEvent(models.Model):
    
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name='submitted_tickets')
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='submitted_tickets')
