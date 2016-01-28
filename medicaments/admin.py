from django.contrib import admin
from .models import Medicament, Famille, Compagnie

# Register your models here.
class MedicamentAdmin(admin.ModelAdmin):
    list_display   = ('commercial', 'famille', 'generique', 'compagnie')
    list_filter    = ('generique','compagnie', 'categorie')
    search_fields  = ('commercial', 'generique')


class FamilleAdmin(admin.ModelAdmin):
    list_display   = ('nom')
    search_fields  = ('nom')

class CompagnieAdmin(admin.ModelAdmin):
    list_display   = ('nom', 'pays')
    search_fields  = ('nom', 'pays')


admin.site.register(Medicament)
admin.site.register(Famille)
admin.site.register(Compagnie)
