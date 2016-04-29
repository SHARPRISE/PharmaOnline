from django.contrib import admin
from .models import PharmaMonkey, Contact

# Register your models here.
class PharmaMonkeyAdmin(admin.ModelAdmin):
    list_display = ('nom', 'bio', 'email', 'phone')
    search_fields = ('nom', 'email')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'Last_name', 'email', 'msg_subject', 'timestamp')
    list_filter  = ('Last_name', 'email', 'msg_subject')


admin.site.register(PharmaMonkey)
admin.site.register(Contact)
