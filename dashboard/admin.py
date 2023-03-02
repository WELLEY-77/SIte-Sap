from django.contrib import admin
from .models import ListNotification, ListPedidos

class ListListNotification(admin.ModelAdmin):
    list_display = ('description','stats', 'hour')

admin.site.register(ListNotification, ListListNotification)
admin.site.register(ListPedidos)