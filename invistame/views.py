from django.shortcuts import render, redirect, HttpResponse
from .models import Gasto, Contato
from .forms import InvestimentoForm, ContatoForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import Http404
from django.core.paginator import Paginator

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
        'dados': Gasto.objects.all(),
        'soma' : Gasto.objects.all().aggregate(total=Sum('valor'))
    }
   
 
    return render(request, 'investimentos/listagem.html', context=dados)


def detalhes(request, id_investimento):
    dados = {
        'dados': Gasto.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhes.html', dados)


def editar(request, id_investimento):
    investimento = Gasto.objects.get(pk=id_investimento)
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('listagem')


def excluir(request, id_investimento):
    investimento = Gasto.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('listagem')
    else:
        return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})

def meus_contatos(request):
    contatos =  {
        'contatos': Contato.objects.all()
    }
    
    return render(request, 'agenda/contatos.html', context=contatos)

def ver_contato(request, contato_id):
    try:
        contato =  Contato.objects.get(id=contato_id)
    

        return render(request, 'agenda/detalhes.html', {
            'contato' : contato
        })
    except Contato.DoesNotExist as e:
        raise Http404()

def novo_contato(request):
    if request.method == 'POST':
        contato_form = ContatoForm(request.POST)
        if contato_form.is_valid():
            contato_form.save()
        return redirect('index')
    else:
        contato_form = ContatoForm()
        formulario = {
            'formulario': contato_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)




def busca(request):
    
    dados = {
        'dados': Gasto.objects.all(),
        'soma' : Gasto.objects.all().aggregate(total=Sum('valor'))
    }

    return render(request, 'investimentos/busca.html', context=dados)
