from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.urlresolvers import reverse
from rest_framework.authtoken.models import Token

from accounts.models import Pharmacy

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
    slug        = models.SlugField(blank=True, null=True)
    famille     = models.ForeignKey('Famille', blank=True, null=True)
    compagnie   = models.ForeignKey('Compagnie', blank=True, null=True)
    statut      = models.CharField(max_length= 255)
    verified    = models.DateTimeField(auto_now=True, auto_now_add=False)
    image       = models.ImageField(blank=True, null=True, upload_to="drug_labels")

    def __str__(self):
        return self.commercial

    def get_absolute_url(self):
        return reverse('medicaments:detail', kwargs={'pk': self.pk})

    def get_modification_url(self):
        return reverse('medicaments:modifier', kwargs={'pk': self.pk})

    def get_deletion_url(self):
        return reverse('medicaments:delete', kwargs={'pk': self.pk})

    def last_seen(self):
        return ("Modifie pour la derniere fois le: %s" %(self.verified))

def create_slug(instance, new_slug=None):
    slug = slugify(instance.commercial + '-' + instance.generique)
    if new_slug is not None:
        slug = new_slug
    qs = Medicament.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=slug)
    return slug


def medicament_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

    if instance.stock == 0:
        instance.statut = "Medicament en rupture de Stock"
    elif (instance.stock <= 5):
        instance.statut = "Peu d'unites disponibles"
    else:
        instance.statut = "Medicament en Stock"


pre_save.connect(medicament_pre_save_receiver, sender=Medicament)

@receiver(post_save, sender=Pharmacy)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
