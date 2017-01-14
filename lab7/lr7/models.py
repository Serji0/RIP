from django.contrib import admin
from django.db import models


class Event(models.Model):
    class Meta():
        db_table = 'events'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=30, default='')
    description = models.TextField(default='')
    city = models.CharField(max_length=30, default='')
    quantity = models.IntegerField(default=0)
    max_quantity = models.IntegerField(default=0)


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'city', 'quantity', 'max_quantity', 'percent_quantity')
    search_fields = ['name']
    list_filter = ['city']

    def percent_quantity(self, obj):
        return '{0:.1%}'.format(obj.quantity / obj.max_quantity)
