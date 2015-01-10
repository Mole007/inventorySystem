# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bdp',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('note', models.CharField(max_length=255, blank=True, null=True)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('numIdCard', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=250, blank=True, null=True)),
                ('name', models.CharField(max_length=35)),
                ('surname', models.CharField(max_length=35)),
                ('birthdate', models.DateField()),
                ('address', models.CharField(max_length=250, blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('note', models.CharField(max_length=255, blank=True, null=True)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('city', models.CharField(max_length=65)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('note', models.CharField(max_length=255, blank=True, null=True)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('country', models.CharField(max_length=75)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='mail',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('note', models.CharField(max_length=255, blank=True, null=True)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('kind', models.IntegerField(choices=[(1, 'Private'), (2, 'Public'), (3, 'Coorporative')])),
                ('mail', models.CharField(max_length=50)),
                ('bdp', models.ForeignKey(to='main.bdp')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='phone',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('note', models.CharField(max_length=255, blank=True, null=True)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('kind', models.IntegerField(choices=[(1, 'Mobil'), (2, 'Home'), (3, 'Coorporative')])),
                ('code', models.IntegerField(blank=True, null=True)),
                ('area', models.IntegerField(blank=True, null=True)),
                ('phone', models.IntegerField()),
                ('bdp', models.ForeignKey(to='main.bdp')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='city',
            name='contry',
            field=models.ForeignKey(to='main.country'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bdp',
            name='city',
            field=models.ForeignKey(to='main.city'),
            preserve_default=True,
        ),
    ]
