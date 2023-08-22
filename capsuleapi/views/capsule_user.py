from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from capsuleapi.models import CapsuleUser


class CapsuleUserView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for a single Capsule User"""

        capsuleuser = CapsuleUser.objects.get(pk=pk)
        serializer = CapsuleUserSerializer(capsuleuser)
        return Response(serializer.data)

    def create(self, request):
        """POST request to create a CapsuleUser"""
        uid = request.META["HTTP_AUTHORIZATION"]

        capsuleuser = CapsuleUser(
            uid=uid,
            first_name=request.data['firstName'],
            last_name=request.data['lastName'],
            email=request.data['email'],
            profile_image=request.data['profileImage'],
        )

        serializer = CapsuleUserSerializer(capsuleuser)
        serializer.is_valid(raise_exception=True)
        serializer.save(uid=uid)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """PUT request to update a Capsule User"""
        capsuleuser = CapsuleUser.objects.get(pk=pk)
        uid = request.META["HTTP_AUTHORIZATION"]
        capsuleuser.first_name = request.data['firstName']
        capsuleuser.last_name = request.data['lastName']
        capsuleuser.email = request.data['email']
        capsuleuser.profile_image = request.data['profileImage']
        capsuleuser.uid = uid
        capsuleuser.save()
        return Response({'message': 'Capsule User Updated'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handles DELETE requests for a Capsule User

        Returns:
            Response -- Empty body with 204 status code
        """
        capsuleuser = CapsuleUser.objects.get(pk=pk)
        capsuleuser.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CapsuleUserSerializer(serializers.ModelSerializer):
    """JSON serializer for Capsule User
    """
    class Meta:
        model = CapsuleUser
        fields = ('id', 'first_name', 'last_name',
                  'email', 'profile_image', 'uid')
        depth = 1
