from django.db import models


from medicaments.models import Medicament

# Create your models here.
class PharmacyProfile(models.Model):
    pharmacy = models.OneToOneField('Medicament')
    active   = models.BooleanField(default="False")

    def __str__(self):
        return self.user.get_full_name
