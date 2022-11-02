"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Gamer


class GamerView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        game_view = Gamer.objects.get(pk=pk)
        serialized = GamerSerializer(game_view, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        game_view = Gamer.objects.all()
        serialized = GamerSerializer(game_view, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class GamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = ('id', 'bio', 'full_name',)