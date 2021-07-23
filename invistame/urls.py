from django.urls import path, include
from . import views

urlpatterns = [
    path('/', include('index.urls')),
    path('/', include('novo_investimento.urls')),
    path('/', include('listagem.urls')),
]
