"""
URL configuration for hellowmenu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cardapio import views 
from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from cardapio.views import lista_produtos, produtos
from django.urls import path
from cardapio.views import cadastrar_produto
from cardapio.views import deletar_produto
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('itensCarrinho/', views.itensCarrinho, name='itensCarrinho'),
    path('localEntrega/', views.localEntrega, name='localEntrega'),
    path('resumoCarrinho/', views.resumoCarrinho, name='resumoCarrinho'),
    path('produtos/', lista_produtos, name='lista_produtos'),
    path('listaprodutos/', produtos, name='listaprodutos'),
    path('produtos/categoria/<int:ID_Categoria>/', lista_produtos, name='produtos_por_categoria'),
    path('produtos/cadastrar/', cadastrar_produto, name='cadastrar-produto'),
    path('produtos/<int:pk>/deletar/', deletar_produto, name='deletar-produto'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)