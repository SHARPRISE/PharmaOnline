"""pharmaonline_beta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls import static
from django.contrib import admin

from medicaments.views import MedicamentList, MedicamentDetail

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accueil/', 'medicaments.views.MedicamentHome', name='accueil'),
    url(r'^inscription$', 'accounts.views.register', name='inscription'),
    url(r'^login/', 'accounts.views.auth_login', name='login'),
    url(r'^produits/', 'medicaments.views.personal_med_list', name='produits'),
    url(r'^logout$', 'accounts.views.auth_logout', name='logout'),
    url(r'^creation/', 'medicaments.views.MedicamentCreate', name='creation'),
    url(r'^modifier/(?P<id>\d+)/$','medicaments.views.MedicamentUpdate', name='modifier'),
    url(r'^(?P<pk>\d+)/$', MedicamentDetail.as_view(), name='detail')
    #url(r'^indexe/$', 'medicaments.views.indexview', name='indexe'),
]
