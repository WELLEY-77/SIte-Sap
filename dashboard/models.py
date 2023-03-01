from django.db import models

class ListNotification(models.Model):
    description = models.CharField('Descrição', max_length=50)
    stats = models.CharField('Estatos', max_length=20)
    hour = models.IntegerField('Horas')

    def __str__(self):
        return self.description
