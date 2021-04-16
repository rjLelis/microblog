# Flask

[Página atual](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)

## Instânciar o flask no arquivo __init__.py do app


```python
# app/__init__.py

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__) # inicializar a aplicação
app.config.from_object(Config) # aplicar as configurações
db = SQLAlchemy(app) # inicializar o banco de dados
migrate = Migrate(app, db) # inicializar o framework de migrations
login = LoginManager(app) # inicializar o framework de autenticação

from . import routes, models
```

* Importar a classe `Config` do arquivo `config.py`, localizado na raiz do projeto

## Criar arquivo de configuração do app na raiz do projeto

```python
# config.py

import os

class Config(object):
    ...
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ...
```

## Criar modulo top-level de inicialização do projeto

```python
# microblog.py

from app import app

```

Rodar `flask run` no terminal inicia o projeto

```shell
$ export FLASK_ENV=microblog
$ flask run
```

## Dependências e suas funções

* flask-wtf - formulários
* flask-sqlalchemy - banco de dados relacional
* flask-migrate - migrações de banco de dados
* flask-login - autenticação
* flask-dotenv - usar arquivo de variáveis de ambiente `.flaskenv`


## Formulários

* Todos as classes formulários vão herdar da classe `flask_wtf.FlaskForm`

* Os campos são do tipo da classe `wtforms.<Tipo>`

* Os validadores de campo vem do pacote `wtforms.validators`

* Validadores:

    * `validators.DataRequired()`

* Tipos de campos

    * `wtforms.StringField('label', validators=[lista_de_validadores])`
    * `wtforms.PasswordField('label', validators=[lista_de_validadores])`
    * `wtforms.BooleanField('label')`
    * `wtforms.SubmitField('label')`

## Banco de dados

### Adicionar as seguintes configurações na classe no `config.py`

```python
    SQLACHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASEDIR, 'app.db')

    SQLACHEMY_TRACK_MODIFICATIONS = False
```

* Todas a classes modelos vão herdar da classe `db.Model`

* Os atributos são do tipo da classe `db.Column`, passando o tipo real pelo construtor dessa classe

* Tipo de dados:

    * `db.String(<quantidade_de_caracteres>)`
    * `db.Integer`
    * `db.DateTime`
    * `db.ForeignKey('<relação.id>')`

* Relacionamento One to Many

Criar uma referencia da relação tanto na tabela `One` quanto na `Many`

* Na tabela com referencia `One`, usar o `db.relationship()`
* Na tabela com referencia `Many`, usar o `db.Column` com o segundo argumento `db.ForeignKey('id')`

```python
# app/models.py

from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'))

```

* O comando `flask db init` cria o repositorio de `migrations`

* O comando `flask db migrate -m "<mensagem>"` cria uma `migration`

* O comando `flask db upgrade` aplica as `migrations`

* O comando `flask db downgrade` desfaz a última `migration`

## Autenticação

* Adicionar as funcionalidades importantes para autenticação na tabela de usuarios

```python
from flask_login import UserMixin

class User(UserMixin, db.Model):
    ...

```

* Criar função para pegar usuário logado

```python
from . import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
```

* Pegar usuário logado

```python
from flask_login import current_user
```

* Função de logar o usuário

```python
from flask_login import login_user
```

* Função de deslogar o usuário

```python
from flask_login import logout_user
```

* Decorator de login exigido

```python
from flask import render_template
from flask_login import login_required
from . import app


@app.route('/')
@login_required
def home():
    return render_template('index.html')
```
