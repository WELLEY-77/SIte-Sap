from django.shortcuts import render
from .models import ListProdutos, CateProdutos

def produtos(request):

    produtos = ListProdutos.objects.all()
    cate_produtos = CateProdutos.objects.all()

    dados = {
        'produtos':produtos,
        'cate_produtos':cate_produtos,
    }

    return render(request, 'produtos/produtos.html', dados)
