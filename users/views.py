from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def novo_usuario(request):
    formulario = UserCreationForm()
    return render(request, 'users/registrar.html', {'formulario':formulario})