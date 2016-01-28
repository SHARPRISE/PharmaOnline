from django.db import models

# Create your models here.
class PharmaMonkey(models.Model):
    nom = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(required=True)
    phone = models.IntegerField()
    picture = models.ImageField()
    pass

    __str__(self):
    return self.nom
