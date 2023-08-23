from django.db import models

class CapsuleUser(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    profile_image = models.CharField(max_length=500)
    uid = models.CharField(max_length=200, default='')
