# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicaments', '0002_auto_20160116_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicament',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
    ]
