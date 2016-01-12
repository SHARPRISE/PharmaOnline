from django.contrib import admin
from .models import Medicament, Famille, Compagnie

# Register your models here.
admin.site.register(Medicament)
admin.site.register(Famille)
admin.site.register(Compagnie)
