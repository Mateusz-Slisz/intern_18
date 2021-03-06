# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-31 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('H1', 'Hero 1 won'), ('H2', 'Hero 2 won')], max_length=2)),
                ('fight_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('won_matches', models.PositiveSmallIntegerField(default=0)),
                ('lost_matches', models.PositiveSmallIntegerField(default=0)),
                ('existence', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='hero',
            name='hero_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saakar.Type'),
        ),
        migrations.AddField(
            model_name='fight',
            name='hero_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hero_1', to='saakar.Hero'),
        ),
        migrations.AddField(
            model_name='fight',
            name='hero_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hero_2', to='saakar.Hero'),
        ),
    ]
