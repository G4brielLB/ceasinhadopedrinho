from django.urls import path

# Importa as Views que a gente crioy
from .views import CampoCreate, VerduraCreate
from .views import CampoUpdate, VerduraUpdate
from .views import CampoDelete, VerduraDelete
from .views import CampoList, VerduraList, VerduraTotalList


#Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/verduras/', VerduraCreate.as_view(), name='cadastrar-verduras'),
    #path('cadastrar/ceasa/', CeasaCreate.as_view(), name='cadastrar-verduras'),



    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),   
    path('editar/verduras/<int:pk>', VerduraUpdate.as_view(), name='editar-verduras'), 

    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),
    path('excluir/verduras/<int:pk>/', VerduraDelete.as_view(), name='excluir-verduras'),
    

    path('listar/campos/', CampoList.as_view(), name='listar-campos'),
    path('listar/verduras/user', VerduraList.as_view(), name='listar-verduras'),
    path('listar/verduras/', VerduraTotalList.as_view(), name='listar-verduras-total')


    #path('endereço/', MinhaView.as_view(), name='nome-da-url')
    
]
