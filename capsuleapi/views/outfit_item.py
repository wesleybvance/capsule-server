from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from capsuleapi.models import Item, Outfit, OutfitItem


class OutfitItemView(ViewSet):
    """Capsule API OutfitItem view"""

    def retrieve(self, request, pk):
        """Gets an outfit_item by its pk

        Returns:
            Response --  single JSON serialized outfit dictionary
        """
        outfit_item = OutfitItem.objects.get(pk=pk)
        serializer = OutfitItemSerializer(outfit_item)
        return Response(serializer.data)

    def list(self, request):
        """Gets outfit items by outfit id

        Returns:
            Response -- JSON serialized list of outfit_items
        """
        outfit_items = OutfitItem.objects.all()
        outfit = request.query_params.get('outfitId', None)

        if outfit is not None:
            outfit_items = outfit_items.filter(outfit_id=outfit)
        serializer = OutfitItemSerializer(outfit_items, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handles POST operations

        Returns:
            Response -- JSON serialized outfit item instance
        """
        outfit = Outfit.objects.get(pk=request.data["outfitId"])
        item = Item.objects.get(pk=request.data["itemId"])
        outfit_item = OutfitItem.objects.create(
            item_id=item,
            outfit_id=outfit,
        )
        serializer = OutfitItemSerializer(outfit_item)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handles PUT requests for an outfit item

        Returns:
            Response -- Empty body with 204 status code
        """
        outfit_item = OutfitItem.objects.get(pk=pk)
        outfit = Outfit.objects.get(pk=request.data["outfitId"])
        item = Item.objects.get(pk=request.data["itemId"])
        outfit_item.outfit_id = outfit
        outfit_item.item_id = item

        outfit_item.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handles DELETE requests for an outfit item

        Returns:
            Response -- Empty body with 204 status code
        """
        outfit_item = OutfitItem.objects.get(pk=pk)
        outfit_item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class OutfitItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitItem
        fields = ('id', 'outfit_id', 'item_id')
        depth = 2
