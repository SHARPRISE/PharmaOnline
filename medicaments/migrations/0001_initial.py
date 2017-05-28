# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Compagnie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('pays', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Famille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commercial', models.CharField(max_length=255)),
                ('generique', models.CharField(max_length=255)),
                ('quantite', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('stock', models.IntegerField()),
                ('slug', models.SlugField(default='slug-field')),
                ('statut', models.CharField(max_length=16)),
                ('verified', models.DateTimeField(auto_now=True)),
                ('compagnie', models.ForeignKey(null=True, to='medicaments.Compagnie', blank=True)),
                ('famille', models.ForeignKey(null=True, to='medicaments.Famille', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
