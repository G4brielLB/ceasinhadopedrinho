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
              'pepino': 0, 'pimenta_de_cheiro': 0, 'pimentao': 0, 'tangerina': 0, 'tomate': 0, 'rucula': 0, 'quiabo': 0}
# Create your models here.

class Campo(models.Model):
    nome = models.CharField(max_length=50, help_text='Digite o nome igual o do seu Login.')
    data = models.DateField(default=date.today)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    

    def __str__(self):
        return ("{} ({})".format(self.nome, self.data))








#class PrintableModel(models.Model):
    #def __repr__(self):
        #return str(self.to_dict())

    #def to_dict(verduras):
        #ceasinha = verduras._meta
        #data = {}
        #for f in chain(ceasinha.concrete_fields, ceasinha.private_fields):
            #data[f.name] = f.value_from_object(verduras)
        #for f in ceasinha.many_to_many:
            #data[f.name] = [i.id for i in f.value_from_object(ceasinha)]
        #return data

    #class Meta:
        #abstract = True

# Só um model teste, praticamente igual a model Verdura
class CeasaModel(models.Model):
    for v in vegetables.keys():
        v = models.IntegerField(default=0)

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

Verdura.objects.all().update()

def to_dict(Verdura):
    opts = Verdura._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields):
        data[f.name] = f.value_from_object(Verdura)
    for f in opts.many_to_many:
        data[f.name] = [i.id for i in f.value_from_object(Verdura)]
    return data

class FinalModel(models.Model):
    verdurafinal = {'Abacate': 0, 'Abacaxi': 0, 'Abobrinha': 0,
                    'Alface': 0, 'Alho Poró': 0, 'Batata': 0,
                    'Batata Doce': 0, 'Brócolis': 0,
                    'Cabeca de Alho': 0, 'Cebola': 0,
                    'Cebola Roxa': 0, 'Cenoura': 0, 'Côco': 0,
                    'Cheiro Verde': 0, 'Chuchu': 0, 'Couve Flor': 0,
                    'Couve Folha': 0, 'Dúzia de Banana': 0,
                    'Espinafre': 0, 'Laranja': 0, 'Maçã': 0,
                    'Macaxeira': 0, 'Mamão': 0, 'Maracujá': 0,
                    'Pepino': 0, 'Pimenta de Cheiro': 0, 'Pimentão': 0, 'Tangerina': 0, 'Tomate': 0, 'Rúcula': 0, 'Quiabo': 0}

    data_atual = date.today()
    c = 0
    quant = list()
    listas = dict()
    lista_final = dict()
    tamanho = len(Verdura.objects.all())

    for a, b in enumerate(Verdura.objects.all()):
        listas[a] = to_dict(b)

    for n in range(0, tamanho):
        if listas[n]['data'] == data_atual:
            lista_final[c] = listas[n]
            c += 1

    for di in lista_final:
        for k, v in lista_final[di].items():
            if k not in 'iddatausuario':
                vegetables[k] += v

    for v in vegetables.values():
        quant.append(v)

    for n, k in enumerate(verdurafinal.keys()):
        verdurafinal[k] += quant[n]
        verdurafinal.update()

    def __str__(self):
        return(f"Lista Total {date.today()}")



