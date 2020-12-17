"""
Definition of models.
"""

from django.db import models
# Create your models here.

class Chord(models.Model):
        '''Model to define a Chord. Chords will be presented with a shape assuming standard tuning. 
        This presentation will be a list of 6 integers representing a fret on each string from low to high (EADGBE)
        '''
        Name = models.CharField(max_length=15)
        Presentation = models.JSONField()

class Song(models.Model):
        '''Model to define a Song. A Song will include lyrics, title, reference URL and artist.
        The song will be 
        '''
        Title = models.CharField(max_length=100)

