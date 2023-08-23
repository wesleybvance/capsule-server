from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from capsuleapi.models import Item, CapsuleUser, Category


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

    def create(self, request):
        """Handles POST operations

        Returns:
            Response -- JSON serialized item instance
        """
        category = Category.objects.get(pk=request.data["categoryId"])
        user = CapsuleUser.objects.get(pk=request.data["uid"])
        item = Item.objects.create(
            category_id=category,
            user_id=user,
            photo_url=request.data["photoUrl"],
            name=request.data["name"],
        )
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handles PUT requests for an item

        Returns:
            Response -- Empty body with 204 status code
        """
        item = Item.objects.get(pk=pk)
        user = CapsuleUser.objects.get(pk=request.data["userId"])
        item.user_id = user
        category = Category.objects.get(pk=request.data["categoryId"])
        item.category_id = category
        item.photo_url = request.data["photoUrl"]
        item.name = request.data["name"]

        item.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handles DELETE requests for an item

        Returns:
            Response -- Empty body with 204 status code
        """
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ItemSerializer(serializers.ModelSerializer):
    """JSON serializer for items
    """
    class Meta:
        model = Item
        fields = ('id', 'name', 'category_id', 'photo_url', 'user_id')
