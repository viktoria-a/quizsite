# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer1',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer2',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer3',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(max_length=300),
        ),
    ]
