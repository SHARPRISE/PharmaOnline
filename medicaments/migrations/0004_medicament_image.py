# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicaments', '0003_auto_20160116_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicament',
            name='image',
            field=models.FileField(null=True, blank=True, upload_to=''),
        ),
    ]
