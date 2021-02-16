from django.urls import path

# Importa as Views que a gente crioy
from .views import CampoCreate, AtividadeCreate, VerduraCreate
from .views import CampoUpdate, AtividadeUpdate
from .views import CampoDelete, AtividadeDelete
from .views import CampoList, AtividadeList, VerduraList


#Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('cadastrar/verduras/', VerduraCreate.as_view(), name='cadastrar-verduras'),
    #path('cadastrar/ceasa/', CeasaCreate.as_view(), name='cadastrar-verduras'),



    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),    
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),

    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),
    path('excluir/atividade/<int:pk>/',
         AtividadeDelete.as_view(), name='excluir-atividade'),

    path('listar/campos/', CampoList.as_view(), name='listar-campos'),
    path('listar/atividades', AtividadeList.as_view(), name='listar-atividades'),
    path('listar/verduras', VerduraList.as_view(), name='listar-verduras')


    #path('endereço/', MinhaView.as_view(), name='nome-da-url')
    
]
