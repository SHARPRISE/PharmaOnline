from django.db import models

# Create your models here.
class PharmaMonkey(models.Model):
    nom = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField()
    phone = models.IntegerField()
    #picture = models.ImageField()

    def __str__(self):
        return self.nom

class Contact(models.Model):
    first_name  = models.CharField(max_length = 100)
    Last_name   = models.CharField(max_length = 50)
    email       = models.EmailField()
    msg_subject = models.CharField(max_length = 30)
    message     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add = True, auto_now = False)

    def __str__(self):
        return self.email
