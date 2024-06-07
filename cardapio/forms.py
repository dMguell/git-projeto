from django import forms
from .models import Produto, Categoria

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['ID_Categoria', 'img', 'name', 'dsc', 'price']
        labels = {
            'ID_Categoria': 'Categoria',
            'img': 'Imagem',
            'name': 'Nome',
            'dsc': 'Descrição',
            'price': 'Preço'
        }
        help_texts = {
            'ID_Categoria': 'Id da categoria do produto',
            'img': 'Imagem do produto',
            'name': 'Nome do produto',
            'dsc': 'Descrição do produto',
            'price': 'Preço do produto'
        }
        widgets = {
            'dsc': forms.Textarea(attrs={'cols': 40, 'rows': 5})
        }