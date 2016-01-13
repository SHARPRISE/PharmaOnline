from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings

from django.utils.text import slugify
# Create your models here.

class Famille(models.Model):
    nom         = models.CharField(max_length= 255)
    description = models.TextField()

    def __str__(self):
        return self.nom

class Compagnie(models.Model):
    nom  = models.CharField(max_length= 255)
    pays = models.CharField(max_length= 255, blank=True)

    def __str__(self):
        return self.nom

class Medicament(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    commercial  = models.CharField(max_length= 255)
    generique   = models.CharField(max_length= 255)
    quantite    = models.CharField(max_length= 255)
    description = models.TextField()
    stock       = models.IntegerField()
    slug        = models.SlugField(default="slug-field")
    famille     = models.ForeignKey('Famille', blank=True, null=True)
    compagnie   = models.ForeignKey('Compagnie', blank=True, null=True)
    statut      = models.CharField(max_length= 16)
    verified  = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.commercial

    def last_seen(self):
        return ("Disponible pour la derniere fois le: %s" %(self.repere))

def create_slug(instance, new_slug=None):
    slug = slugify(instance.commercial + '-' + instance.generique)
    if new_slug is not None:
        slug = new_slug
    qs = Medicaments.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=slug)
    return slug


def medicament_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    elif instance.stock == 0:
        instance.statut = "Medicament en rupture de Stock"
    elif (instance.stock <= 5):
        instance.statut = "Peu d'unites disponibles"
    else:
        instance.statut = "Medicament en Stock"

pre_save.connect(medicament_pre_save_reciever, sender=Medicament)
