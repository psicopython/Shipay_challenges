from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# instanciando os objetos
db = SQLAlchemy()
mi = Migrate()

# configuração do db
def config_db(app):
	
	# configurando SQLAlchemy
	db.init_app(app)
	# eu costumo fazer isso para evitar "circular import"
	app.db = db
	
	# Configurando Migrate
	mi.init_app(app,app.db)


# Agora que o arquivo já esta carregado,
# importamos as tabelas,
# que usam apenas os models do SQLAlchemy
# (se existir 500 tabelas, eu farei isso 500x ou crio uma função)
from . import transacoes 