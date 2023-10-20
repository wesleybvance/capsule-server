from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from capsuleapi.models import Item, CapsuleUser, Category, Tag

class TagView(ViewSet):
    """Capsule Tag view"""

    def retrieve(self, request, pk):
        """Gets a tag by its pk
        
        Returns:
          Response -- single JSON serialized item dictionary
        """
        tag = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)
    
    def list(self, request):
        """Gets all tags
        
        Returns:
            Response -- JSON serialized list of items
        """
        
        tags = Tag.objects.all()
        uid = request.query_params.get('uid', None)
        if uid is not None:
            tags = tags.filter(user_id=uid)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handles POST operations 
        
        Returns: 
            Response -- JSON serialized tag instance
        """
        user = CapsuleUser.objects.get(pk=request.data["uid"])
        tag = Tag.objects.create(
            user_id=user,
            name=request.data["name"],
        )
        serializer = TagSerializer(tag)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handles PUT request for a tag
        
        Returns:
            Response -- Empty body with 204 status code
        """
        tag = Tag.objects.get(pk=pk)
        user = CapsuleUser.objects.get(pk=request.data["userId"])
        tag.user_id = user
        tag.request.data["name"]
        
        tag.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy (self, request, pk):
        """Handles DELETE requests for a tag
        
        Returns:
            Response -- Empty body with 204 status code
        """
        tag = Tag.objects.get(pk=pk)
        tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
        

class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for tags
    """
    
    class Meta:
      model = Tag
      fields = ('id', 'name', 'user_id')
        
