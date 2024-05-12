from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from capsuleapi.models import Tag, Outfit, OutfitTag


class OutfitTagView(ViewSet):
    """Capsule API OutfitTag view"""

    def retrieve(self, request, pk):
        """Gets an outfit_tag by pk

        Returns:
            Response -- single JSON serialized outfit_tag dictionary
        """

        outfit_tag = OutfitTag.objects.get(pk=pk)
        serializer = OutfitTagSerializer(outfit_tag)
        return Response(serializer.data)

    def list(self, request):
        """Gets outfit_tags by outfit_id

        Returns:
            Response -- JSON serialized list of outfit_tags
        """
        outfit_tags = OutfitTag.objects.all()
        outfit = request.query_params.get("outfitId", None)

        if outfit is not None:
            outfit_tags = outfit_tags.filter(outfit_id=outfit)

        serializer = OutfitTagSerializer(outfit_tags, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handles POST operations

        Returns:
            Response -- JSON serialized outfit_tag instance
        """
        outfit = Outfit.objects.get(pk=request.data["outfitId"])
        tag = Tag.objects.get(pk=request.data["tagId"])
        outfit_tag = OutfitTag.objects.create(
            tag_id=tag,
            outfit_id=outfit,
        )
        serializer = OutfitTagSerializer(outfit_tag)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handles PUT requests for an outfit_tag

        Returns:
            Response -- Empty body with 204 status code
        """

        outfit_tag = OutfitTag.objects.get(pk=pk)
        outfit = Outfit.objects.get(pk=request.data["outfitId"])
        tag = Tag.objects.get(pk=request.data["tagId"])
        outfit_tag.outfit_id = outfit
        outfit_tag.tag_id = tag

        outfit_tag.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handles DELETE requests for an outfit tag

        Returns:
            Response -- Empty body with 204 status code
        """
        outfit_tag = OutfitTag.objects.get(pk=pk)
        outfit_tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class OutfitTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitTag
        fields = ("tag_id", "id", "outfit_id")
