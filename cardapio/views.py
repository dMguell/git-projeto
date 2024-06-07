from django.shortcuts import render
from .models import Produto
from django.shortcuts import render, redirect


from django.shortcuts import render, redirect
from .models import Produto, Categoria

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    produtos = Produto.objects.all()  # Busca todos os produtos se nenhum ID de categoria for fornecido
    return render(request, 'home.html', {'produtos': produtos})

def itensCarrinho(request):
    return render(request, 'itensCarrinho.html')

def localEntrega(request):
    return render(request, 'localEntrega.html')

def resumoCarrinho(request):
    return render(request, 'resumoCarrinho.html')

@login_required
def lista_produtos(request, ID_Categoria=None):
    if ID_Categoria:
        produtos = Produto.objects.filter(ID_Categoria=ID_Categoria)  # Filtra produtos por categoria
    else:
        produtos = Produto.objects.all()  # Busca todos os produtos se nenhum ID de categoria for fornecido
    return render(request, 'menu.html', {'produtos': produtos})

def produtos(request):
    return render(request, 'listaprodutos.html')
    
# def cadastrar_produto(request):
#     if request.method == 'POST':
#         form = ProdutoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('cadastrar-produto')  # Redirecionar para a página de produtos
#     else:
#         form = ProdutoForm()
#     return render(request, 'cadastrar_produto.html', {'form': form})

# def cadastrar_produto(request):
#     if request.method == 'POST':
#         ID_Categoria = request.POST.get('ID_Categoria')
#         img = request.FILES.get('img')
#         name = request.POST.get('name')
#         dsc = request.POST.get('dsc')
#         price = request.POST.get('price')
        
#         categoria = Categoria.objects.get(id=ID_Categoria) if ID_Categoria else None
        
#         novo_produto = Produto(
#             ID_Categoria=categoria,
#             img=img,
#             name=name,
#             dsc=dsc,
#             price=price
#         )
#         novo_produto.save()
        
#         return redirect('')  # Redirecionar para a página de listagem de produtos após o cadastro
#     else:
#         categorias = Categoria.objects.all()
#         return render(request, 'cadastrar_produto.html', {'categorias': categorias})

# def deletar_produto(request, pk):
#     produto = get_object_or_404(Produto, pk=pk)
#     if request.method == 'POST':
#         produto.delete()
#         return redirect('lista-produtos')
#     return render(request, 'produto_confirm_delete.html', {'produto': produto})

@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        ID_Categoria = request.POST.get('ID_Categoria')
        img = request.FILES.get('img')
        name = request.POST.get('name')
        dsc = request.POST.get('dsc')
        price = request.POST.get('price')
        
        categoria = Categoria.objects.get(id=ID_Categoria) if ID_Categoria else None
        
        novo_produto = Produto(
            ID_Categoria=categoria,
            img=img,
            name=name,
            dsc=dsc,
            price=price
        )
        novo_produto.save()
        
        return redirect('cadastrar-produto')  # Redirecionar para a página de listagem de produtos após o cadastro
    else:
        categorias = Categoria.objects.all()
        produtos = Produto.objects.all()
        return render(request, 'cadastrar_produto.html', {'categorias': categorias, 'produtos': produtos})

@login_required
def deletar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('cadastrar-produto')
    return render(request, 'produto_confirm_delete.html', {'produto': produto})