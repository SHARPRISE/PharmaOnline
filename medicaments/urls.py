from django.conf import settings
from django.conf.urls import url, include

from .models import Medicament

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    home,
    # create_medicament,
    update_medicament,
    MedicamentCreate,
    MedicamentDetail,
    MedicamentDelete,
    public_med_list,
    personal_med_list,
    CreateView,
    DetailsView
    )

urlpatterns = [
    url(r'^ajouter', MedicamentCreate.as_view(), name="ajouter"),
    url(r'^delete/(?P<pk>\d+)/$', MedicamentDelete.as_view(), name='delete'),
    url(r'^modifier/(?P<pk>\d+)/$', update_medicament, name="modifier"),
    url(r'^medicaments', public_med_list, name="liste-publique"),
    url(r'^inventaire', personal_med_list, name='inventaire'),
    url(r'^item/(?P<pk>\d+)/$', MedicamentDetail.as_view(), name='detail'),
    # url(r'^newmeds/$', CreateView.as_view(), name='create'),
    # url(r'^newmeds/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    # url(r'^get-token/', obtain_auth_token),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
