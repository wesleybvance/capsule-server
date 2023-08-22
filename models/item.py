from django.db import models
from .category import Category
from .capsule_user import CapsuleUser

class Item(models.Model):

    name = models.CharField(max_length=200)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    photo_url = models.CharField(max_length=500)
    user_id = models.ForeignKey(CapsuleUser, on_delete=models.CASCADE)
