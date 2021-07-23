from django.forms import ModelForm, fields
from .models import Investimento


class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__'
