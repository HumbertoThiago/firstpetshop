from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.shortcuts import render, get_object_or_404

from django.urls import reverse_lazy

from .models import Cliente, Animal, Raca, Pet, Servico, Hospedagem

class IndexView(TemplateView):
    template_name = "dashboard.html"    

class ClienteCreate(CreateView):
    login_url = reverse_lazy('login')
    model = Cliente
    fields = ['foto', 'nome', 'rg', 'cpf', 'cidade', 'uf', 'telefone', 'email']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-cliente')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Clientes"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

class AnimalCreate(CreateView):
    login_url = reverse_lazy('login')
    model = Animal
    fields = ['nome']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-animal')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Animais"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

class RacaCreate(CreateView):
    login_url = reverse_lazy('login')
    model = Raca
    fields = ['nome']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-raca')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Raças"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

class PetCreate(CreateView):
    login_url = reverse_lazy('login')
    model = Pet
    fields = ['foto', 'nome', 'idade', 'cliente', 'raca', 'animal', 'cor_predominante']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-pet')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Pets"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context
    
class ServicoCreate(CreateView):
    login_url = reverse_lazy('login')
    model = Servico
    fields = ['dt_agendada', 'hr_agendada', 'tipo', 'cliente', 'obs']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-servico')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Serviços"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context
    
class HospedagemCreate(CreateView):
    login_url = reverse_lazy('login')
    model = Hospedagem
    fields = ['dt_checkin', 'hr_checkin', 'dt_checkout', 'hr_checkout', 'cliente', 'observacao', 'status']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-hospedagem')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastrar Hospedagem/Reserva"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context      

class ClienteUpdate(UpdateView):
    login_url = reverse_lazy('login')
    model = Cliente
    fields = ['foto', 'nome', 'rg', 'cpf', 'cidade', 'uf', 'telefone', 'email']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-cliente')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro do Cliente"
        context['botao'] = "Salvar"

        return context

class AnimalUpdate(UpdateView):
    login_url = reverse_lazy('login')
    model = Animal
    fields = ['nome']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-animal')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro de Tipo de Animal"
        context['botao'] = "Salvar"

        return context

class RacaUpdate(UpdateView):
    login_url = reverse_lazy('login')
    model = Raca
    fields = ['nome']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-raca')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro de Raças"
        context['botao'] = "Salvar"

        return context

class PetUpdate(UpdateView):
    login_url = reverse_lazy('login')
    model = Pet
    fields = ['foto', 'nome', 'idade', 'cliente', 'raca', 'animal', 'cor_predominante']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-pet')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro do Pet"
        context['botao'] = "Salvar"
        
        return context

class ServicoUpdate(UpdateView):
    login_url = reverse_lazy('login')
    model = Servico
    fields = ['dt_agendada', 'hr_agendada', 'tipo', 'cliente', 'obs']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-servico')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro de Serviço"
        context['botao'] = "Salvar"

        return context    
    
class HospedagemUpdate(UpdateView):
    login_url = reverse_lazy('login')
    model = Hospedagem
    fields = ['dt_checkin', 'hr_checkin', 'dt_checkout', 'hr_checkout', 'cliente', 'observacao', 'status']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-hospedagem')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro de Hospedagem/Reserva"
        context['botao'] = "Salvar"

        return context     

class ClienteDelete(DeleteView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('listar-cliente')

class AnimalDelete(DeleteView):
    login_url = reverse_lazy('login')
    model = Animal
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('listar-animal')

class RacaDelete(DeleteView):
    login_url = reverse_lazy('login')
    model = Raca
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('listar-raca')

class PetDelete(DeleteView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('listar-pet')
    
class ServicoDelete(DeleteView):
    login_url = reverse_lazy('login')
    model = Servico
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('listar-servico')   
    
class HospedagemDelete(DeleteView):
    login_url = reverse_lazy('login')
    model = Hospedagem
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('listar-hospedagem')     

class ClienteList(ListView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'clientes/clientes.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['campo_pesquisa'] = "nome"
        
        return context

    def get_queryset(self):

        txt_nome = self.request.GET.get('inptPesquisar')

        if txt_nome:
            clientes = Cliente.objects.filter(nome__icontains=txt_nome)
        else:
            clientes = Cliente.objects.all()

        return clientes

class AnimalList(ListView):
    login_url = reverse_lazy('login')
    model = Animal
    template_name = 'animais/animais.html'
    paginate_by = 10

    def get_queryset(self):

        txt_nome = self.request.GET.get('inptPesquisar')

        if txt_nome:
            animais = Animal.objects.filter(nome__icontains=txt_nome)
        else:
            animais = Animal.objects.all()

        return animais

class RacaList(ListView):
    login_url = reverse_lazy('login')
    model = Raca
    template_name = 'racas/racas.html'
    paginate_by = 10

    def get_queryset(self):

        txt_nome = self.request.GET.get('inptPesquisar')

        if txt_nome:
            racas = Raca.objects.filter(nome__icontains=txt_nome)
        else:
            racas = Raca.objects.all()

        return racas

class PetList(ListView):
    login_url = reverse_lazy('login')
    model = Pet
    template_name = 'pets/pets.html'
    paginate_by = 10

    def get_queryset(self):

        txt_nome = self.request.GET.get('inptPesquisar')

        if txt_nome:
            pets = Pet.objects.filter(nome__icontains=txt_nome)
        else:
            pets = Pet.objects.all()

        return pets

class ServicoList(ListView):
    login_url = reverse_lazy('login')
    model = Servico
    template_name = 'servicos/servicos.html'
    paginate_by = 10

    def get_queryset(self):

        txt_nome = self.request.GET.get('inptPesquisar')

        if txt_nome:
            servicos = Servico.objects.filter(nome__icontains=txt_nome)
        else:
            servicos = Servico.objects.all()

        return servicos

class HospedagemList(ListView):
    login_url = reverse_lazy('login')
    model = Hospedagem
    template_name = 'hospedagens/hospedagens.html'
    paginate_by = 10

    def get_queryset(self):

        txt_nome = self.request.GET.get('inptPesquisar')

        if txt_nome:
            hospedagens = Hospedagem.objects.filter(nome__icontains=txt_nome)
        else:
            hospedagens = Hospedagem.objects.all()

        return hospedagens

class ProntuarioView(TemplateView):
    template_name = "prontuario.html"  
