from django.shortcuts import render


def index(request):
    return render(request, 'investimentos/index.html')
