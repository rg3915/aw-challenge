# aw-challenge

AW Challenge

## Objetivo

Construir uma nova aplicação, utilizando o framework de sua preferência, a qual deverá conectar na API do GitHub e disponibilizar as seguintes funcionalidades:

- Botão para buscar e armazenar os repositórios destaques de 5 linguagens à sua escolha;
- Listar os repositórios encontrados;
- Visualizar os detalhes de cada repositório.

Alguns requisitos:

- Deve ser uma aplicação totalmente nova;
- A solução deve estar em um repositório público do GitHub;
- A aplicação deve armazenar as informações encontradas;
- Utilizar PostgreSQL, MySQL ou SQL Server;
- O deploy deve ser realizado, preferencialmente, no Heroku ou no Azure;
- A aplicação precisa ter testes automatizados.

## Clonando e rodando a api localmente

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.

```
git clone https://github.com/rg3915/aw-challenge.git
cd aw-challenge
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py test
python manage.py runserver
```

## App

https://aw-challenge-regis.herokuapp.com/

## O que foi usado

* Python 3.6.6
* Django 2.2.1
* VueJS 2.6.10
* Bootstrap 4.0
