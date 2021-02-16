from django.views.generic import TemplateView

# Create your views here.
class PaginaInicial(TemplateView):
    template_name = 'index.html'

class SobreView(TemplateView):
    #template_name = 'sobre.html'
    template_name = 'sobre.html'

class TesteView(TemplateView):
    template_name = 'teste.html'

