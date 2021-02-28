from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from itertools import chain


vegetables = {'abacate': 0, 'abacaxi': 0, 'abobrinha': 0,
              'alface': 0, 'alho_poro': 0, 'batata': 0,
              'batata_doce': 0, 'brocolis': 0,
              'cabeca_de_alho': 0, 'cebola': 0,
              'cebola_roxa': 0, 'cenoura': 0, 'coco': 0,
              'cheiro_verde': 0, 'chuchu': 0, 'couve_flor': 0,
              'couve_folha': 0, 'banana': 0,
              'espinafre': 0, 'laranja': 0, 'maca': 0,
              'macaxeira': 0, 'mamao': 0, 'maracuja': 0,
              'pepino': 0, 'pimenta_de_cheiro': 0, 'pimentao': 0,
              'tangerina': 0, 'tomate': 0, 'rucula': 0, 'quiabo': 0}
# Create your models here.

class Campo(models.Model):
    nome = models.CharField(max_length=50, help_text='Digite o nome igual o do seu Login.')
    data = models.DateField(default=date.today)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    

    def __str__(self):
        return ("{} ({})".format(self.nome, self.data))

class Verdura(models.Model):
    data = models.DateField(default=timezone.now)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    #vegetables = {'Abacates': 1, 'Abacaxis': 1, 'Abobrinhas': 1,
    #              'Alfaces': 1, 'Alhos Porós': 1, 'Bananas': 1}
    abacate = models.IntegerField(default=0)
    abacaxi = models.IntegerField(default=0)
    abobrinha = models.IntegerField(default=0)
    alface = models.IntegerField(default=0)
    alho_poro = models.IntegerField(default=0, verbose_name='Alho Poró')
    batata = models.DecimalField(default=0, verbose_name='Batata (kg)', help_text='Quantidade de Batatas x 0.13', decimal_places=2, max_digits=5)
    batata_doce = models.IntegerField(default=0)
    brocolis = models.IntegerField(default=0)
    cabeca_de_alho = models.IntegerField(default=0, verbose_name='Cabeça de Alho')
    cebola = models.DecimalField(default=0, verbose_name='Cebola (kg)', max_digits=5, decimal_places=2, help_text='Quantidade de Cebolas x 0.15')
    cebola_roxa = models.IntegerField(default=0, verbose_name='Cebola Roxa')
    cenoura = models.DecimalField(default=0, verbose_name='Cenoura (kg)',
                                  help_text='Quantidade de Cenouras x 0.2', decimal_places=2, max_digits=5)
    coco = models.IntegerField(default=0)
    cheiro_verde = models.IntegerField(default=0, verbose_name='Cheiro Verde')
    chuchu = models.IntegerField(default=0)
    couve_flor = models.IntegerField(default=0, verbose_name='Couve Flor')
    couve_folha = models.IntegerField(default=0, verbose_name='Couve Folha')
    banana = models.DecimalField(
        default=0, verbose_name='Dúzias de Banana',
         decimal_places=2, max_digits=5, help_text='Dúzias em valor decimal.')
    espinafre = models.IntegerField(default=0)
    laranja = models.IntegerField(default=0)
    maca = models.IntegerField(default=0, verbose_name='Maçã')
    macaxeira = models.IntegerField(default=0)
    mamao = models.IntegerField(default=0, verbose_name='Mamão')
    maracuja = models.IntegerField(default=0, verbose_name='Maracujá')
    pepino = models.IntegerField(default=0)
    pimenta_de_cheiro = models.IntegerField(default=0, verbose_name='Pimenta de Cheiro')
    pimentao = models.IntegerField(default=0, verbose_name='Pimentão')
    tangerina = models.IntegerField(default=0)
    tomate = models.DecimalField(default=0, decimal_places=2, max_digits=5, help_text='Quantidade de Tomates x 0.15')
    rucula = models.IntegerField(default=0, verbose_name='Rúcula')
    quiabo = models.IntegerField(default=0)
    
    def __str__(self):
        return(f"Lista {self.usuario} {self.data}")


def to_dict(Verdura):
    opts = Verdura._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields):
        data[f.name] = f.value_from_object(Verdura)
    for f in opts.many_to_many:
        data[f.name] = [i.id for i in f.value_from_object(Verdura)]
    return data

class FinalModel:
    def __init__(self, verdurafinal):
        self.verdurafinal = verdurafinal

    def resultado(self):
        data_atual = date.today()
        count = 0
        verduras = Verdura.objects.all()
        quant = list()
        listas = dict()
        lista_final = dict()
        tamanho = len(verduras)

        for a, b in enumerate(verduras):
            listas[a] = to_dict(b)

        for n in range(0, tamanho):
            if listas[n]['data'] == data_atual:
                lista_final[count] = listas[n]
                count += 1

        for di in lista_final:
            for k, v in lista_final[di].items():
                if k not in 'iddatausuario':
                    vegetables[k] += v

        for v in vegetables.values():
            quant.append(v)
        
        for n, k in enumerate(self.verdurafinal.keys()):
            self.verdurafinal[k] += quant[n]      
            
        lista = dict((k, v) for k, v in self.verdurafinal.items() if v > 0)
        for k in vegetables.keys():
            vegetables[k] = 0
 
        for k in self.verdurafinal.keys():
            self.verdurafinal[k] = 0      

        return(lista)
    
    def __str__(self):
        return(f"Lista Total {date.today()}")
   


