"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event



class EventView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        
        Returns:
            Response -- JSON serialized game type
        """
        event_type = Event.objects.get(pk=pk)
        serialized = Event.Serializer(event_type, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests to get all event types

        Returns:
            Response -- JSON serialized list of event types
        """

        event_types = Event.objects.all()
        serializer = Event.Serializer(event_types, many=True)
        return Response(serializer.data)

class Event.Serializer(serializers.ModelSerializer):
    """JSON serializer for game types"""

    class Meta:
        model = EventType
        fields = ('id', 'label',)