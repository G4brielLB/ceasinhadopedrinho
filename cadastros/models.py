from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils import timezone

abacate = abacaxi = abobrinha = alface = alho_poro = banana = 0
vegetables = {'abacate': 1, 'abacaxi': 1, 'abobrinha': 1,
              'alface': 1, 'alho_poro': 1, 'batata': 1,
              'batata_doce': 1, 'brocolis': 1,
              'cabeca_de_alho': 1, 'cebola': 1,
              'cebola_roxa': 1, 'cenoura': 1, 'coco': 1,
              'cheiro_verde': 1, 'chuchu': 1, 'couve_flor': 1,
              'couve_folha': 1, 'banana': 1,
              'espinafre': 1, 'laranja': 1, 'maca': 1,
              'macaxeira': 1, 'mamao': 1, 'maracuja': 1,
              'pepino': 1, 'pimenta_de_cheiro': 1, 'pimentao': 1, 'tangerina': 1, 'tomate': 1, 'rucula': 1, 'quiabo': 1}
lista_final = dict()
# Create your models here.

class Campo(models.Model):
    nome = models.CharField(max_length=50, help_text='Digite o nome igual o do seu Login.')
    data = models.DateField(default=date.today)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    

    def __str__(self):
        return ("{} ({})".format(self.nome, self.data))

class Verdura(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    data = models.DateField(default=timezone.now)
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

# Só um model teste, praticamente igual a model Verdura
class CeasaModel(models.Model):
    for v in vegetables.keys():
        v = models.IntegerField(default=0)







