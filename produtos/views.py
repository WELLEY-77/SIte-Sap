from django.shortcuts import render
from .models import ListProdutos

def produtos(request):

    produtos = ListProdutos.objects.all()

    dados = {
        'produtos':produtos,
    }

    return render(request, 'produtos/produtos.html', dados)
