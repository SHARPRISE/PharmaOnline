from django.conf import settings
from django.conf.urls import url
from .views import contact

urlpatterns = [
    url(r'^message', contact, name="message-us"),
]
