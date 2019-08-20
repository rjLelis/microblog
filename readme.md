# Flask

## Instânciar o flask no arquivo __init__.py do app

* Importar a classe `Config` do arquivo `config.py`, localizado na raiz do projeto

```python
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import routes, models
```

## Criar arquivo de configuração do app na raiz do projeto

```python
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
```

## Dependências e suas funções

* flask-wtf - formulários
* flask-sqlalchemy - banco de dados relacional
* flask-migrate - migrações de banco de dados
* flask-dotenv - usar arquivo de variáveis de ambiente `.flaskenv`


## Formulários

* Todos as classes formulários vão herdar da classe `flask_wtf.FlaskForm`

* Os campos são do tipo da classe `wtforms.<Tipo>`

* Os validadores vem do pacote `wtforms.validators`

* Validadores:

    * `validators.DataRequired()`

* Tipos de campos

    * `wtforms.StringField('label', validators=[lista_de_validadores])`
    * `wtforms.PasswordField('label', validators=[lista_de_validadores])`
    * `wtforms.BooleanField('label')`
    * `wtforms.SubmitField('label')`

## Banco de dados

### Adicionar as seguintes configurações no `config.py`

```python
    SQLACHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
        
    SQLACHEMY_TRACK_MODIFICATIONS = False
```

* Todas a classes modelos vão herdar da classe `db.Model`

* Os atributos são do tipo da classe `db.Column`, passando o tipo real pelo construtor dessa classe

* Tipo de dados:

    * `db.String(<quantidade_de_caracteres>)`
    * `db.Interger`
    * `db.DateTime`
    * `db.ForeignKey('<relação.id>')`

* O comando `flask db init` criar os scripts ddl

* O comando `flask db migrate -m <mensagem>` aplica os scripts ddl