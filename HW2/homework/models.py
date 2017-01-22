from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


class Good(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30, default='')
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    logo = models.ImageField(upload_to='images/')
    user_comment = models.ManyToManyField(User, through='Comment', related_name='users')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    text = models.TextField(default='')
