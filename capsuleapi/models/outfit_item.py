from django.db import models
from .outfit import Outfit
from .item import Item

class OutfitItem(models.Model):

    name = models.CharField(max_length=100)
    outfit_id = models.ForeignKey(Outfit, on_delete=models.CASCADE, related_name="outfitId")
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="itemId")
