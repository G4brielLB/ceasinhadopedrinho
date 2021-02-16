from django.contrib import admin

# Register your models here.

from .models import Campo, Atividade, Verdura, CeasaModel

admin.site.register(Campo)
admin.site.register(Atividade)
admin.site.register(Verdura)