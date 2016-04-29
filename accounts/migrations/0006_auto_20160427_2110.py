# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20160423_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='horaire',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='phone_number',
            field=models.CharField(blank=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")], max_length=30),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='proprietaire',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
