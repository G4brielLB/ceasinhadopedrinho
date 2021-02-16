from django.forms import ModelForm
from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import Verdura

class VerduraForm(forms.ModelForm):
    class Meta:
        model = Verdura
        fields = [
            'abacate', 'abacaxi', 'abobrinha',
            'alface', 'alho_poro', 'banana'
        ]
