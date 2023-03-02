from django.shortcuts import render
from .models import ListNotification, ListPedidos

def dashboard(request):

    lista_notificao = ListNotification.objects.all()
    lista_pedidos = ListPedidos.objects.all()

    dados = {
        'lista_notificacao':lista_notificao,
        'lista_pedidos':lista_pedidos,
    }

    return render(request, 'dashboard/index.html', dados)
