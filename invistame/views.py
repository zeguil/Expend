from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento, Contato
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

def index(request):
    return render(request, 'investimentos/index.html')


def novo_investimento(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('index')
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)

@login_required
def listagem(request):
    dados = {
        'dados': Investimento.objects.all(),
        'soma' : Investimento.objects.all().aggregate(total=Sum('valor'))
    }
   
 
    return render(request, 'investimentos/listagem.html', context=dados)


def detalhes(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhes.html', dados)


def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('listagem')


def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('listagem')
    else:
        return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})

def contatos(request):
    contatos = {
        'contatos': Contato.objects.all()
    }

    return render(request, 'agenda/contatos.html', context=contatos)

def ver_contato(request, id_contato):
    contato = {
        'contato': Contato.objects.get(pk=id_contato)
    }

    return render(request, 'agenda/detalhes.html', contato)






