from django.db import models
from .capsule_user import CapsuleUser

class Tag(models.Model):

    name = models.CharField(max_length=500)
    user_id = models.ForeignKey(CapsuleUser, on_delete=models.CASCADE, related_name="capsuleUser")
