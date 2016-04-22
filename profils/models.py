from django.db import models


from medicaments.models import Medicament

# Create your models here.
class PharmacyProfile(models.Model):
    pharmacy = models.OneToOneField('Medicament')
    adresse  = models.CharField("")
    #phone   = models.IntegerField()
    active   = models.BooleanField(default="False")
    #ajouter horaire de la pharmacie

    def __str__(self):
        return self.user.get_full_name

class ClientProfile(models.Model):
    prenom   = models.CharField(max_length=255)
    nom      = models.CharField(max_length=255)
    adresse  = models.CharField(max_length=255)
    #phone   = models.IntegerField()
