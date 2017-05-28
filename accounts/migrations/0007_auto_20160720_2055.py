# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20160427_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('address', models.CharField(max_length=255, blank=True)),
                ('phone_number', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='pharmacy',
            old_name='address',
            new_name='addresse',
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='horaire',
            field=models.TextField(),
        ),
    ]
