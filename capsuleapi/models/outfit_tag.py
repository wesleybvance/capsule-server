from django.db import models
from .tag import Tag
from .outfit import Outfit

class OutfitTag(models.Model):

    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="tag")
    outfit_id = models.ForeignKey(Outfit, on_delete=models.CASCADE, related_name="outfit")
