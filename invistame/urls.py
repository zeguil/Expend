from django.urls import path
from . import views
from users import views as userviews

urlpatterns = [
    path('', views.index, name='index'),
    path('conta/', userviews.novo_usuario, name='novo_usuario'),
    path('novo_investimento/', views.novo_investimento, name='novo_investimento'),
    path('novo_investimento/<int:id_investimento>', views.editar, name='editar'),
    path('listagem/', views.listagem, name='listagem'),
    path('detalhes/<int:id_investimento>', views.detalhes, name='detalhes'),
    path('excluir/<int:id_investimento>', views.excluir, name='excluir')
]
