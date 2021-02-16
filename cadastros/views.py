from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Verdura
from .forms import VerduraForm
from .models import Campo, Atividade, Verdura, CeasaModel
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

vegetables = {'Abacates': 1, 'Abacaxis': 1, 'Abobrinhas': 1,
              'Alfaces': 1, 'Alhos Porós': 1, 'Bananas': 1}

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

#class CeasaCreate(FormView):
    #template_name = 'cadastros/ceasa.html'
    #form_class = CeasaForm
    #success_url = reverse_lazy('index')
    #def ceasa(self, request):
        #ceasa = {}
        #form = CeasaForm(request.POST or None)
        #if form.is_valid():
            #form.save

        #ceasa['form'] = form
        #return render(request, 'ceasa.html', ceasa)

class AtividadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')

class VerduraCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u'Família'
    login_url = reverse_lazy('login')
    vegetables = {'Abacates': 1, 'Abacaxis': 1, 'Abobrinhas': 1,
               'Alfaces': 1, 'Alhos Porós': 1, 'Bananas': 1}
    model = Verdura
    fields = ['abacate', 'abacaxi', 'abobrinha',
           'alface', 'alho_poro', 'banana']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

    def form_valid(self, form):

        # Antes do super não foi criado o objeto
        form.instance.usuario = self.request.user

        url = super().form_valid(form)
        # Depois do super o objeto foi criado
        return url
    def ceasa(self, request):
        ceasa = {}
        form = VerduraForm(request.POST or None)
        if form.is_valid():
            form.save

        ceasa['form'] = form
        return render(request, 'ceasa.html', ceasa)




############# UPDATE ###############

class CampoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u'Família'
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['nome', 'data']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

class AtividadeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros.form.html'
    reverse_lazy('index')

############# DELETE ###############

class CampoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u'Família'
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')

class AtividadeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

############# LISTA ###############

class CampoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/listas/campo.html'

    def get_queryset(self):

        self.object_list = Campo.objects.filter(usuario=self.request.user)
        return self.object_list

class AtividadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'

class VerduraList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Verdura
    template_name = 'cadastros/listas/verduras.html'




