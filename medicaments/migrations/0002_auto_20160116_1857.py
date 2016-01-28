# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicaments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicament',
            name='statut',
            field=models.CharField(max_length=255),
        ),
    ]
