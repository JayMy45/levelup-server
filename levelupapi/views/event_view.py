"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event
from levelupapi.models.gamer import Gamer



class EventView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        
        Returns:
            Response -- JSON serialized game type
        """
        event_type = Event.objects.get(pk=pk)
        serialized = EventSerializer(event_type, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests to get all event types

        Returns:
            Response -- JSON serialized list of event types
        """

        # set event_type equal to empty list 
        events = []

        # if there is a query string parameter 'game' then filter ...
        if "game" in request.query_params:
            events = Event.objects.filter(game__id=request.query_params['game'])

        else:
            events = Event.objects.all()

        serialized = EventSerializer(events, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

class EventOrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = ('id', 'bio', 'full_name')


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for game types"""
    organizer = EventOrganizerSerializer(many=False)

    class Meta:
        model = Event
        fields = ('id', 'organizer', 'game', 'description','organizer',)

        depth = 1