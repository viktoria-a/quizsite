# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20150813_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='imagelink',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
