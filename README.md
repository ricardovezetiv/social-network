# social-network
Rede Social simples e divertida! Crie o seu usuário, publique mensagens e siga outros usuários.

# Para instalar

### Obtendo repositório

1. Faça login no github
2. Crie um **fork** (cópia) deste repositório clicando em [fork](https://github.com/ricardovezetiv/social-network/fork)
3. O seu repositório estará em `https://github.com/username/social-network`
4. Copie a URL do seu repositório

> **Observação**: substitua `username` pelo seu nome de usuário do github.

### Preparando o ambiente

- Você pode executar localmente no seu computador desde que tenha no mínimo o Python 3.8
  - Para rodar localmente faça o clone com `git clone https://github.com/username/social-network`
  - Acesse a pasta `social-network`
- Ou em qualquer plataforma que permita executar Python 3.8

## Requisitos

Este template utiliza o gerenciador de pacotes **poetry**, para instalar o Poetry:

### Ambiente Windows
Se estiver rodando no Windows no seu ambiente local, execute o comando abaixo
no `Windows PowerShell` para instalar o Poetry

```bash
$ (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

### Ambiente Linux
Se estiver rodando no Linux no seu ambiente local, execute o comando abaixo
para instalar o Poetry

```bash
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

## Instalando o ambiente

O comando a seguir instala as dependências do projeto.

```bash
$ poetry install
```

O comando a seguir ativa o ambiente virtual do poetry

```bash
$ poetry shell
```

> **Importante:** o ambiente precisa estar ativado.

Executando o programa

```bash
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

### Via browser

Acessar os links `http://127.0.0.1:8000/`

## Comandos utilizados no desenvolvimento

```bash
$ poetry config virtualenvs.in-project true
```

- Abrir o projeto Git com o PyCharm
- Configurar o Poetry como **'Python Interpreter'** no PyCharm

```bash
$ poetry shell
$ poetry add django
$ poetry add flake8 black --dev

$ poetry show --tree
$ django-admin --version

$ django-admin startproject project .
$ python manage.py startapp social_app
```

- Configurar o **'Run/Debug Configurations'** no PyCharm com base no comando `$ python manage.py runserver`

```bash
$ python manage.py migrate
$ python manage.py createsuperuser

$ python manage.py makemigrations
$ python manage.py migrate

$ poetry add fontawesomefree

$ flake8 .
$ black -l 79 --check --diff .
```

> **Observação:** No término do projeto, o nome da aplicação foi alterado para `social` e o código foi refatorado. 

> Projeto inspirado no passo-a-passo do link abaixo
https://realpython.com/django-social-network-1/
