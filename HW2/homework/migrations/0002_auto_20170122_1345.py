# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-22 10:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('description', models.TextField(default='')),
                ('price', models.IntegerField(default=0)),
                ('logo', models.ImageField(upload_to='images/')),
                ('user_comment', models.ManyToManyField(related_name='users', through='homework.Comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.AddField(
            model_name='comment',
            name='good',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.Good'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]