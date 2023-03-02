from django.db import models

class ListProdutos(models.Model):
    name = models.CharField('Nome', max_length=50)
    unidade = models.IntegerField('Unidades vendidas')
    em_estoque = models.CharField('Em estoque', max_length=8)
    date = models.DateField('Data', auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.name}'


class CateProdutos(models.Model):
    categoria = models.CharField('Categoria', max_length=50)
