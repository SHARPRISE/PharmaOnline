# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160422_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacyuser',
            name='owner_first_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacyuser',
            name='owner_last_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
