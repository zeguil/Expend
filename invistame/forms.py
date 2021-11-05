from django.forms import ModelForm, fields
from .models import Gasto, Contato


class InvestimentoForm(ModelForm):
    class Meta:
        model = Gasto
        fields = '__all__'

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'