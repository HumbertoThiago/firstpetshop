# FirstPetShop

Sistema gestor das informações de prestação de serviços de um Pet Shop, desenvolvido na Disciplina de Projeto Integrador II do curso de Engenharia da Computação pela Universidade Virtual do Estado de São Paulo (UNIVESP)

EM DESENVOLVIMENTO...

DICAS DE COMANDOS USADOS:

# AMBIENTE VIRTUAL 
python -m venv .venv

# ATIVANDO O AMBIENTE
.\.venv\Scripts\activate

# ATUALIZANDO PIP
py -m pip install --upgrade pip

# INSTALAR DJANGO
pip install django

# INICIAR PROJETO
django-admin startproject setup .

# TESTANDO SERVIDOR
py manage.py runserver 8080

# INICIAR APLICATIVO PRINCIPAL 
py manage.py startapp firstpetshop

# INICIAR APLICATIVO LOGIN
py manage.py startapp accounts

# INSTALAR PLUGIN FORMATAÇÃO 
pip install crispy-bootstrap5

# INSTALAR PLUGIN IMAGENS
py install pillow

# CHECAR ALTERAÇÕES DO MODELO
manage.py makemigrations

# ENVIA ALTERAÇÕES DO MODELO PARA O BD
py manage.py migrate

# CRIAR SUPER USUÁRIO PARA PRIMEIRO LOGIN
py manage.py createsuperuser

