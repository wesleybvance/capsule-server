from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from capsuleapi.models import Item, Outfit

class ItemView(ViewSet):
    """Capsule Item view"""

    def retrieve(self, request, pk):
        """Gets an item by its pk

        Returns:
            Response --  single JSON serialized item dictionary
        """
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)


class ItemSerializer(serializers.ModelSerializer):
    """JSON serializer for items
    """
    class Meta:
        model = Item
        fields = ('id', 'name', 'category_id', 'photo_url', 'user_id')
