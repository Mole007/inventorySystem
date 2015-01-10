# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('note', models.CharField(max_length=255, blank=True, null=True)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('area', models.CharField(max_length=45)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('bdp_ptr', models.OneToOneField(serialize=False, to='main.bdp', auto_created=True, primary_key=True, parent_link=True)),
                ('gender', models.IntegerField(choices=[(1, 'Hombre'), (2, 'Mujer'), (3, 'Otro')])),
            ],
            options={
                'abstract': False,
            },
            bases=('main.bdp',),
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('bdp_ptr', models.OneToOneField(serialize=False, to='main.bdp', auto_created=True, primary_key=True, parent_link=True)),
                ('kind', models.IntegerField(choices=[(1, 'Privada'), (2, 'Publica'), (3, 'Mixta')])),
            ],
            options={
                'abstract': False,
            },
            bases=('main.bdp',),
        ),
        migrations.CreateModel(
            name='companyContact',
            fields=[
                ('bdp_ptr', models.OneToOneField(serialize=False, to='main.bdp', auto_created=True, primary_key=True, parent_link=True)),
                ('gender', models.IntegerField(choices=[(1, 'Hombre'), (2, 'Mujer'), (3, 'Otro')])),
                ('company', models.ForeignKey(to='client.company')),
            ],
            options={
                'abstract': False,
            },
            bases=('main.bdp',),
        ),
        migrations.CreateModel(
            name='kindClient',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('note', models.CharField(max_length=255, blank=True, null=True)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('kind', models.CharField(max_length=35)),
                ('credictMax', models.FloatField()),
                ('discount', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='responsible',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('note', models.CharField(max_length=255, blank=True, null=True)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('responsible', models.CharField(max_length=45)),
                ('area', models.ForeignKey(to='client.area')),
                ('company', models.ManyToManyField(to='client.company', through='client.companyContact')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='companycontact',
            name='responsible',
            field=models.ForeignKey(to='client.responsible'),
            preserve_default=True,
        ),
    ]
