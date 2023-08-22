from django.db import models
from .capsule_user import CapsuleUser

class Outfit(models.Model):

    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(CapsuleUser, on_delete=models.CASCADE)
