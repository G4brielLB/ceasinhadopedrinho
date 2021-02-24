from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Campo, Verdura, to_dict, FinalModel
from .forms import VerduraForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from datetime import date


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

# Create your views here.
class CampoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u'Família'
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['nome', 'data']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cadastrar-verduras')

    def form_valid(self, form):

        # Antes do super não foi criado o objeto
        form.instance.usuario = self.request.user

        url = super().form_valid(form)
        # Depois do super o objeto foi criado
        return url

class CeasaCreate(FormView):
    template_name = 'cadastros/ceasa.html'
    form_class = VerduraForm
    success_url = reverse_lazy('index')
    def ceasa(self, request):
        ceasa = {}
        form = VerduraForm(request.POST or None)
        if form.is_valid():
            form.save()

        ceasa['form'] = form
        return render(request, 'ceasa.html', ceasa)

class VerduraCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u'Família'
    login_url = reverse_lazy('login')
    model = Verdura
    a = []
    for v in vegetables.keys():
        a.append(v)
    fields = a.copy()
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-verduras')

    def form_valid(self, form):

        # Antes do super não foi criado o objeto
        form.instance.usuario = self.request.user

        url = super().form_valid(form)
        # Depois do super o objeto foi criado
        return url
    def ceasa(self, request):
        ceasa = {}
        form = VerduraForm(request.POST)
        if form.is_valid():
            form.save()

        ceasa['form'] = form
        #return render(request, 'ceasa.html', ceasa)'''




############# UPDATE ###############

class CampoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u'Família'
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['nome', 'data']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')


class VerduraUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u'Família'
    login_url = reverse_lazy('login')
    model = Verdura
    a = []
    for v in vegetables.keys():
        a.append(v)
    fields = a.copy()    
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-verduras')

############# DELETE ###############

class CampoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u'Família'
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')

class VerduraDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u'Família'
    login_url = reverse_lazy('login')
    model = Verdura
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-verduras')

############# LISTA ###############

class CampoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/listas/campo.html'

    def get_queryset(self):

        self.object_list = Campo.objects.filter(usuario=self.request.user)
        return self.object_list


class VerduraList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Verdura
    template_name = 'cadastros/listas/verduras.html'

    def get_queryset(self): 

        self.object_list = Verdura.objects.filter(usuario=self.request.user)
        return self.object_list

class VerduraTotalList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Verdura
    template_name = 'cadastros/listas/verduras.html'


    def get_queryset(self):

        self.object_list = Verdura.objects.all()
        return self.object_list




class FinalList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = FinalModel
    template_name = 'cadastros/listas/final.html'

    def get_queryset(self):          
        self.object_list = FinalModel.verdurafinal
        return self.object_list
