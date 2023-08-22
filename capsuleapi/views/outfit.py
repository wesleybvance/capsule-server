from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from capsuleapi.models import Item, Outfit, CapsuleUser, Category


class OutfitView(ViewSet):
    """Capsule API Outfit view"""

    def retrieve(self, request, pk):
        """Gets an outfit by its pk

        Returns:
            Response --  single JSON serialized outfit dictionary
        """
        outfit = Outfit.objects.get(pk=pk)
        serializer = OutfitSerializer(outfit)
        return Response(serializer.data)

    def list(self, request):
        """Gets outfits by user

        Returns:
            Response -- JSON serialized list of flight bookings
        """
        outfits = Outfit.objects.all()
        user = request.query_params.get('uid', None)
        if user is not None:
            outfits = outfits.filter(user_id=user)
        serializer = OutfitSerializer(outfits, many=True)
        return Response(serializer.data)


class OutfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outfit
        fields = ('name', 'user_id')
        depth = 1
