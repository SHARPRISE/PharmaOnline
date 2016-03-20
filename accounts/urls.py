from django.conf import settings
from django.conf.urls import include, url, static

from .views import register, auth_login, auth_logout

urlpatterns = [
    url(r'^inscription', register, name='inscription'),
    url(r'^identification', auth_login, name='indentification'),
    url(r'^deconnection', auth_logout, name='deconnection'),
]
