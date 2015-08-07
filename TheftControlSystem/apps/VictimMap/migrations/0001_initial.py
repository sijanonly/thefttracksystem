# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.DecimalField(null=True, max_digits=12, decimal_places=9, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=12, decimal_places=9, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('phone', models.TextField(null=True, blank=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('place', models.ForeignKey(related_name='end', blank=True, to='VictimMap.Place', null=True)),
            ],
        ),
    ]
