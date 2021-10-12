from django.forms import ModelForm, fields
from .models import Medicos, Pacientes

class pacienteForm(ModelForm):
    class Meta:
        model = Pacientes
        fields = ['nome','telefone', 'endereco', 'numero', 'cidade', 'uf', 'pais', 'cep', 'data']

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.fields['cep'].widget.attrs.update({'class': 'mask-cep'})
        self.fields['cep'].widget.attrs.update({'onblur': 'pesquisacep(this.value);'})
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})
        self.fields['pais'].widget.attrs.update({'value': 'Brasil'})
        
        # <!-- onblur="pesquisacep(this.value); -->

class medicoForm(ModelForm):
    class Meta:
        model = Medicos
        fields = ['nome', 'email', 'senha', 'data']
        