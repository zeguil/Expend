from django.shortcuts import render
from .models import Investimento


def index(request):
    return render(request, 'investimentos/index.html')


def novo_investimento(request):
    return render(request, 'investimentos/novo_investimento.html')


def listagem(request):
    dados = {
        'dados':Investimento.objects.all()
    }
    return render(request, 'investimentos/listagem.html', context=dados)


def detalhes(request,id_investimento):
    dados = {
        'dados':Investimento.objects.get(pk=id_investimento)
        }
    return render(request, 'investimentos/detalhes.html', dados)
