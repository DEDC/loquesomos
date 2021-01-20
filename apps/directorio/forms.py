# Django
from django import forms
# App directorio
# --- models
from .models import Categorias, Repartidores, Directorio

class fRegistroCategorias(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(fRegistroCategorias, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categorias.objects.filter(categoria__isnull = True)

class fRegistroRepartidores(forms.ModelForm):
    class Meta:
        model = Repartidores
        fields = '__all__'
    
class fRegistroDirectorio(forms.ModelForm):
    class Meta:
        model = Directorio
        fields = '__all__'

class fMunicipios(forms.Form):
    municipios = forms.ChoiceField(choices = Directorio.municipios_choices, label_suffix = '', initial = 'centro')
