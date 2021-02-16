from django.urls import path

# Importa as Views que a gente crioy
from .views import PaginaInicial, SobreView, TesteView

#Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    #path('endereço/'), MinhaView.as_view(), name='nome-da-url'
    path('', PaginaInicial.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('teste/', TesteView.as_view(), name='teste')
]