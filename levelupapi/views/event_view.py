"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Game, Gamer




class EventView(ViewSet):
    """Level up game types view"""

    @action(methods=['post'], detail=True)
    def signup(self, request, pk):
        """Post request for a user to sign up for an event"""
    
        gamer = Gamer.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.add(gamer)
        return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)
    


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

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        organizer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])
       
        event = Event.objects.create(
            game=game,
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            organizer=organizer,
        )

        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        event = Event.objects.get(pk=pk)
        event.description = request.data["description"]
        event.date = request.data["date"]
        event.time = request.data["time"]

        game = Game.objects.get(pk=request.data["game"])
        event.game = game
        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)  

    def destroy(self, request, pk):
            event = Event.objects.get(pk=pk)
            event.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
            

class EventOrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = ('id', 'bio', 'full_name')


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for game types"""
    organizer = EventOrganizerSerializer(many=False)

    class Meta:
        model = Event
        fields = ('id', 'organizer', 'game', 'description','organizer', 'date', 'time', 'attendees' )
