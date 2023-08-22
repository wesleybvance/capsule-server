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

    def list(self, request):
        """Gets all items

        Returns:
            Response -- JSON serialized list of items
        """
        items = Item.objects.all()
        uid = request.query_params.get('uid', None)
        category = request.query_params.get('category', None)
        if uid is not None:
            if category is not None:
                items = items.filter(user_id=uid, category_id=category)
            else:
                items = items.filter(user_id=uid)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


class ItemSerializer(serializers.ModelSerializer):
    """JSON serializer for items
    """
    class Meta:
        model = Item
        fields = ('id', 'name', 'category_id', 'photo_url', 'user_id')
