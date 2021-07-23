from django.shortcuts import render


def index(request):
    return render(request, 'investimentos/index.html')


def novo_investimento(request):
    return render(request, 'investimentos/novo_investimento.html')


def listagem(request):
    return render(request, 'investimentos/listagem.html')


def detalhes(request):
    return render(request, 'investimentos/detalhes.html')
