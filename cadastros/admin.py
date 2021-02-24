from django.contrib import admin

# Register your models here.

from .models import Campo, Verdura

admin.site.register(Campo)
admin.site.register(Verdura)
