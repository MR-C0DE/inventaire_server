from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Inventaire(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    sorte = models.CharField(max_length=200)
    quantite = models.IntegerField()
    seuil = models.IntegerField()

    def __getElement__(self):
        return [self.nom]
