from django.urls import path

# Importa as Views que a gente crioy
from .views import CampoCreate, VerduraCreate
from .views import CampoUpdate 
from .views import CampoDelete
from .views import CampoList, VerduraList


#Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/verduras/', VerduraCreate.as_view(), name='cadastrar-verduras'),
    #path('cadastrar/ceasa/', CeasaCreate.as_view(), name='cadastrar-verduras'),



    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),    

    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),

    path('listar/campos/', CampoList.as_view(), name='listar-campos'),
    path('listar/verduras', VerduraList.as_view(), name='listar-verduras')


    #path('endereço/', MinhaView.as_view(), name='nome-da-url')
    
]
