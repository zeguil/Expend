from django.forms import ModelForm, fields
from .models import Investimento, Contato


class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__'

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'