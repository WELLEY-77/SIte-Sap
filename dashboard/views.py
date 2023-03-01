from django.shortcuts import render
from .models import ListNotification

def dashboard(request):

    lista_notificao = ListNotification.objects.all()

    dados = {
        'lista_notificacao':lista_notificao
    }

    return render(request, 'dashboard/index.html', dados)
