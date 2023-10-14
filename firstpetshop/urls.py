from django.urls import path
from .views import IndexView, ProntuarioView
from .views import ClienteCreate, ClienteUpdate, ClienteDelete, ClienteList
from .views import AnimalCreate, AnimalUpdate, AnimalDelete, AnimalList
from .views import RacaCreate, RacaUpdate, RacaDelete, RacaList
from .views import PetCreate, PetUpdate, PetDelete, PetList
from .views import ServicoCreate, ServicoUpdate, ServicoDelete, ServicoList
from .views import HospedagemCreate, HospedagemUpdate, HospedagemDelete, HospedagemList

#from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='dashboard'),

    path('cadastrar/cliente/', ClienteCreate.as_view(), name="cadastrar-cliente"),
    path('editar/cliente/<int:pk>/', ClienteUpdate.as_view(), name="editar-cliente"),
    path('excluir/cliente/<int:pk>/', ClienteDelete.as_view(), name="excluir-cliente"),
    path('listar/cliente/', ClienteList.as_view(), name="listar-cliente"),
    
    path('cadastrar/animal/', AnimalCreate.as_view(), name="cadastrar-animal"),
    path('editar/animal/<int:pk>/', AnimalUpdate.as_view(), name="editar-animal"),
    path('excluir/animal/<int:pk>/', AnimalDelete.as_view(), name="excluir-animal"),
    path('listar/animal/', AnimalList.as_view(), name="listar-animal"),

    path('cadastrar/raca/', RacaCreate.as_view(), name="cadastrar-raca"),
    path('editar/raca/<int:pk>/', RacaUpdate.as_view(), name="editar-raca"),
    path('excluir/raca/<int:pk>/', RacaDelete.as_view(), name="excluir-raca"),
    path('listar/raca/', RacaList.as_view(), name="listar-raca"),

    path('cadastrar/pet/', PetCreate.as_view(), name="cadastrar-pet"),
    path('editar/pet/<int:pk>/', PetUpdate.as_view(), name="editar-pet"),
    path('excluir/pet/<int:pk>/', PetDelete.as_view(), name="excluir-pet"),
    path('listar/pet/', PetList.as_view(), name="listar-pet"),

    path('cadastrar/servico/', ServicoCreate.as_view(), name="cadastrar-servico"),        
    path('editar/servico/<int:pk>/', ServicoUpdate.as_view(), name="editar-servico"),
    path('excluir/servico/<int:pk>/', ServicoDelete.as_view(), name="excluir-servico"),
    path('listar/servico/', ServicoList.as_view(), name="listar-servico"),

    path('cadastrar/hospedagem/', HospedagemCreate.as_view(), name="cadastrar-hospedagem"),        
    path('editar/hospedagem/<int:pk>/', HospedagemUpdate.as_view(), name="editar-hospedagem"),
    path('excluir/hospedagem/<int:pk>/', HospedagemDelete.as_view(), name="excluir-hospedagem"),
    path('listar/hospedagem/', HospedagemList.as_view(), name="listar-hospedagem"),

    path('listar/prontuario/<int:pk>/', ProntuarioView.as_view(), name="listar-prontuario"),
]