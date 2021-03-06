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
from django.conf.urls import include, url, static
from django.contrib import admin



urlpatterns = [
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', 'general.views.landing', name='accueil'),
    url(r'^dashboard', 'general.views.dashboard', name='dashboard'),
    url(r'^about-us', 'general.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('haystack.urls')),
    url(r'^comptes/', include("accounts.urls", namespace="accounts")),
    url(r'^medicaments/', include("medicaments.urls", namespace="medicaments")),
    url(r'^contact/', include("contact_us.urls", namespace="contact_us")),
    url(r'^api/', include('medicaments.rest_urls', namespace="rest_urls"))
]
