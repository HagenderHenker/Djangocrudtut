from django.db import models
from django.urls import reverse


# Create your models here.

class Adressen(models.Model):
    vorname = models.CharField(max_length=50)
    nachname = models.CharField(max_length=50)
    strasse = models.CharField(max_length=100)
    plz = models.IntegerField()
    ort = models.CharField(max_length=100)

    def __str__(self): # Lesbare Repräsentanz jedes Datensatzes nämlich Nachname
        return self.nachname
    
    def get_absolute_url(self): # Die Funktion erzeugt eine kanonische URL für jeden Datensatz
        return reverse('adress_detail', args=[str(self.id)])