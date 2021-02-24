from django.forms import ModelForm
from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import Verdura

vegetables = {'abacate': 1, 'abacaxi': 1, 'abobrinha': 1,
              'alface': 1, 'alho_poro': 1, 'batata': 1,
              'batata_doce': 1, 'brocolis': 1, 'cabeca_de_alho': 1, 'cebola': 1,
              'cebola_roxa': 1, 'cenoura': 1, 'coco': 1,
              'cheiro_verde': 1, 'chuchu': 1, 'couve_flor': 1,
              'couve_folha': 1, 'banana': 1,
              'espinafre': 1, 'laranja': 1, 'maca': 1,
              'macaxeira': 1, 'mamao': 1, 'maracuja': 1,
              'pepino': 1, 'pimenta_de_cheiro': 1, 'pimentao': 1, 'tangerina': 1, 'tomate': 1, 'rucula': 1, 'quiabo': 1}

class VerduraForm(forms.ModelForm):
    class Meta:
        model = Verdura
        a = []
        for v in vegetables.keys():
            a.append(v)
        fields = a.copy()

