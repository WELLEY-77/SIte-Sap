from django.contrib import admin
from .models import ListNotification

class ListListNotification(admin.ModelAdmin):
    list_display = ('description','stats', 'hour')

admin.site.register(ListNotification, ListListNotification)