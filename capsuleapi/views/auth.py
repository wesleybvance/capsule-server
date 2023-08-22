from rest_framework.decorators import api_view
from rest_framework.response import Response
from capsuleapi.models.capsule_user import CapsuleUser
from rest_framework import status


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Capsule User

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    capsuleuser = CapsuleUser.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if capsuleuser is not None:

        data = {
            'id': capsuleuser.id,
            'uid': capsuleuser.uid,
            'first_name': capsuleuser.first_name,
            'last_name': capsuleuser.last_name,
            'email': capsuleuser.email,
            'profile_image': capsuleuser.profile_image
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new Capsule User for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    capsuleuser = CapsuleUser.objects.create(
        uid=request.data['uid'],
        first_name=request.data['firstName'],
        last_name=request.data['lastName'],
        email=request.data['email'],
        profile_image=request.data['profileImage'],
    )

    data = {
        'id': capsuleuser.id,
        'uid': capsuleuser.uid,
        'first_name': capsuleuser.first_name,
        'last_name': capsuleuser.last_name,
        'email': capsuleuser.email,
        'profile_image': capsuleuser.profile_image
    }

    return Response(data)
