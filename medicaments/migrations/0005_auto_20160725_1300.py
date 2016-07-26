# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicaments', '0004_medicament_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicament',
            name='image',
            field=models.ImageField(null=True, upload_to='drug_labels', blank=True),
        ),
    ]
