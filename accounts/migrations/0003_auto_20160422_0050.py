# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160421_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pharmacyuser',
            name='owner_first_name',
        ),
        migrations.RemoveField(
            model_name='pharmacyuser',
            name='owner_last_name',
        ),
    ]
