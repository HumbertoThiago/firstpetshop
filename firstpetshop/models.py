from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class MyProfile(models.Model):
    user = models.OneToOneField(User, 
						on_delete=models.CASCADE, related_name='profile')
    description = models.CharField(max_length=100)


@receiver(post_save, sender=User)
def my_handler(sender, **kwargs):
    """
    Quando Criar um usuário no Django, vai rodar essa função
    para criar uma instancia nesse modelo MyProfile no campo "user".
    """
    if kwargs.get('created', False):
        MyProfile.objects.create(user=kwargs['instance'])

#MyModels

#def upload_foto_cliente(instance, filename):
#    return f"{instance.id_cliente}-{filename}"

class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    rg = models.CharField(max_length=40, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True, verbose_name="endereço")
    cidade = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=120, blank=True, null=True)
    foto = models.ImageField(upload_to='images/', blank=True, null=True)
    #foto = models.ImageField(upload_to=upload_foto_cliente, blank=True, null=True)
    
    def __str__(self):
        return "{} ({})".format(self.nome, self.telefone)

class Raca(models.Model):
    nome = models.CharField(max_length=60, help_text="Digite a Raça do Pet")
    
    def __str__(self) -> str:
        return self.nome
    
class Animal(models.Model):
    nome = models.CharField(max_length=60, help_text="Digite o Tipo de Pet")
    
    def __str__(self) -> str:
        return self.nome 

class Pet(models.Model):
    nome = models.CharField(max_length=60)
    idade = models.IntegerField(blank=True, null=True)    
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    raca = models.ForeignKey(Raca, on_delete=models.PROTECT, verbose_name="raça do pet",)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT, verbose_name="tipo de pet") 
    cor_predominante = models.CharField(max_length=40, verbose_name="cor predominante")
    foto = models.ImageField(upload_to='images/', null=True)
    
    def __str__(self):
        return "{} - ({})".format(self.nome, self.cliente)

class Servico(models.Model):
    SERVICO_TIPO = [
        ("BANHO", "BANHO"),
        ("BANHOTOSA", "BANHO E TOSA"),
        ("TOSA", "TOSA"),
        ("CLINICO", "CLINICO"),
    ]    
    dt_agendada = models.DateField(verbose_name="Data Agendada")
    hr_agendada = models.TimeField(verbose_name="Hora Agendada", blank=True, null=True)
    tipo = models.CharField(max_length=30, choices=SERVICO_TIPO, verbose_name="Tipo de Serviço")
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    obs = models.TextField(max_length=255, verbose_name="Observações")

    def __str__(self):
        return "[{}] {} : {} - {} ({})".format(self.pk, self.dt_agendada, self.hr_agendada, self.cliente, self.tipo)

class ServicoPet(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.servico, self.pet)
    
class Hospedagem(models.Model):
    HOSPEDAGEM_STATUS = [
        ("AGENDADO","AGENDADO"),
        ("CANCELADO","CANCELADO"),
        ("CHECK-IN","CHECK-IN"),
        ("CHECK-OUT","CHECK-OUT"),
        ("RESERVADO","RESERVADO"),
    ]
    dt_agendada = models.DateTimeField(auto_now_add=True, verbose_name="Data Agendada")
    dt_checkin = models.DateField(verbose_name="Data Check-in")
    hr_checkin = models.TimeField(verbose_name="Hora Check-in")
    dt_checkout = models.DateField(verbose_name="Data Check-out")
    hr_checkout = models.TimeField(verbose_name="Hora Check-out")
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    observacao = models.TextField(max_length=255, blank=True, null=True, verbose_name="Observações")
    status = models.CharField(max_length=30, choices=HOSPEDAGEM_STATUS)

    def __str__(self):
        return "[{}] {} : {} - {}".format(self.pk, self.dt_agendada, self.hr_agendada, self.cliente)    

class Quarto(models.Model):
    descricao = models.CharField(verbose_name="descrição", max_length=40)
    numero = models.IntegerField(verbose_name="número do quarto")
    
    def __str__(self):
        return "{} ({})".format(self.descricao, self.numero)    

class HospedagemQuarto(models.Model):
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.PROTECT)
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT)
    quarto = models.ForeignKey(Quarto, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - ({}) - ({})".format(self.hospedagem, self.pet, self.quarto)
