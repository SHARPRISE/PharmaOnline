from django.conf import settings
from django.conf.urls import url

from .views import (
    home,
    create_medicament,
    update_medicament,
    MedicamentList,
    MedicamentDetail,
    public_med_list,
    personal_med_list,
    )

urlpatterns = [
    url(r'^ajouter', create_medicament, name="ajouter"),
    url(r'^modifier/(?P<pk>\d+)/$', update_medicament, name="modifier"),
    url(r'^medicaments', public_med_list, name="liste-publique"),
    url(r'^inventaire', personal_med_list, name='inventaire'),
    url(r'^item/(?P<pk>\d+)/$', MedicamentDetail.as_view(), name='detail'),
]
