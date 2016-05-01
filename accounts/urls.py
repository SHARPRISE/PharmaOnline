from django.conf import settings
from django.conf.urls import url

from .views import (
        register,
        auth_login,
        auth_logout,
        pharmacy_registration,
        bridge,
        )

urlpatterns = [
    url(r'^inscription', register, name='inscription-normale'),
    url(r'^identification', auth_login, name='login'),
    url(r'^deconnection', auth_logout, name='logout'),
    url(r'^pharmacie', pharmacy_registration, name='new_pharmacy'),
    url(r'^choix', bridge, name='account_choice'),
]
