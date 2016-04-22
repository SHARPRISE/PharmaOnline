# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160422_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacyuser',
            name='owner_first_name',
            field=models.CharField(max_length=120, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pharmacyuser',
            name='owner_last_name',
            field=models.CharField(max_length=120, default='Blank'),
            preserve_default=False,
        ),
    ]
