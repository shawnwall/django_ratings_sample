from django.db import models
from djangoratings.fields import AnonymousRatingField

class Thing(models.Model):
    """(Thing description)"""
    name = models.CharField(max_length=100)
    rating = AnonymousRatingField(range=5, can_change_vote=True)
    
    def __unicode__(self):
        return self.name