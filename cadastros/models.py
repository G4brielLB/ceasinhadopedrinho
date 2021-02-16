from django.db import models
from datetime import date
from django.contrib.auth.models import User

vegetables = {'Abacates': 1, 'Abacaxis': 1, 'Abobrinhas': 1,
              'Alfaces': 1, 'Alhos Porós': 1, 'Bananas': 1}
lista_final = dict()
# Create your models here.

class Campo(models.Model):
    nome = models.CharField(max_length=50, help_text='Digite o nome igual o do seu Login.')
    data = models.DateField(default=date.today)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    

    def __str__(self):
        return ("{} ({})".format(self.nome, self.data))

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name='Número')
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    pontos = models.DecimalField(decimal_places=1, max_digits=4)
    detalhes = models.CharField(max_length=100)
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)


    def __str__(self):
        return(f"{self.numero} - {self.descricao} ({self.campo})")


class Verdura(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    data = models.DateField(default=date.today())
    #vegetables = {'Abacates': 1, 'Abacaxis': 1, 'Abobrinhas': 1,
    #              'Alfaces': 1, 'Alhos Porós': 1, 'Bananas': 1}
    abacate = models.IntegerField(default=0)
    abacaxi = models.IntegerField(default=0)
    abobrinha = models.IntegerField(default=0)
    alface = models.IntegerField(default=0)
    alho_poro = models.IntegerField(default=0)
    banana = models.DecimalField(
        default=0, verbose_name='Dúzias de Banana',
         decimal_places=1, max_digits=4, help_text='Dúzias em valor decimal.')


    def __str__(self):
        return(f"Lista {self.usuario} {self.data}")

class CeasaModel(models.Model):
    abacate = models.IntegerField(default=0)
    abacaxi = models.IntegerField(default=0)
    abobrinha = models.IntegerField(default=0)
    alface = models.IntegerField(default=0)
    alho_poro = models.IntegerField(default=0)
    banana = models.DecimalField(
        default=0, verbose_name='Dúzias de Banana', decimal_places=1, max_digits=4, help_text='Dúzias em valor decimal.')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    pessoa = models.ForeignKey(Campo, on_delete=models.PROTECT)

    def __str__(self):
        return(f"Lista {self.usuario}")




