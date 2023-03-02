from django.db import models
from datetime import datetime

class ListNotification(models.Model):
    description = models.CharField('Descrição', max_length=50)
    stats = models.CharField('Estatos', max_length=20)
    hour = models.IntegerField('Horas')

    def __str__(self):
        return self.description

class ListPedidos(models.Model):
    num_pedido = models.IntegerField('Numero do pedido')
    status = models.CharField('Estatus do pedido', max_length=20)
    operation = models.CharField('Operação', max_length=30)
    location = models.CharField('Localização', max_length=35)
    distacia = models.CharField('Distancia',max_length=5)
    date = models.DateTimeField('Data', default=datetime.now, blank=True)
    endereco = models.CharField('Endereço', max_length=50)