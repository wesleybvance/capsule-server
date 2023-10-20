# from django.http import HttpResponseServerError
from django.db.models import Q
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
# from rest_framework.decorators import action
from capsuleapi.models import Item, Outfit, CapsuleUser, Category, Tag, OutfitTag


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
            Response -- JSON serialized list of outfits
        """
        outfits = Outfit.objects.all()
        user = request.query_params.get('uid', None)
        search_text = self.request.query_params.get('q', None)
        tag_id = request.query_params.get('tagId', None)

        if tag_id is not None:
            outfits = outfits.filter(outfit__tag_id=tag_id)
            # otags = outfit_tags.filter(tag_id=tag_id)
            # for otag in otags:
            #     outfit = Outfit.objects.get(pk=otag.outfit_id)
            #     tag_outfits.append(outfit)
            # outfits = tag_outfits
            # print(tag_outfits)
        if user is not None:
            outfits = outfits.filter(user_id=user)
        if search_text is not None:
            outfits = outfits.filter(
                Q(name__contains=search_text)
            )
        serializer = OutfitSerializer(outfits, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handles POST operations

        Returns:
            Response -- JSON serialized outfit instance
        """
        user = CapsuleUser.objects.get(pk=request.data["userId"])
        outfit = Outfit.objects.create(
            user_id=user,
            name=request.data["name"],
        )
        serializer = OutfitSerializer(outfit)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handles PUT requests for an outfit

        Returns:
            Response -- Empty body with 204 status code
        """
        outfit = Outfit.objects.get(pk=pk)
        user = CapsuleUser.objects.get(pk=request.data["userId"])
        outfit.user_id = user
        outfit.name = request.data["name"]

        outfit.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handles DELETE requests for an outfit

        Returns:
            Response -- Empty body with 204 status code
        """
        outfit = Outfit.objects.get(pk=pk)
        outfit.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class OutfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outfit
        fields = ('id', 'name', 'user_id')
        depth = 1
