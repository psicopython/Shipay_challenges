from app.model import config_db
from app.views import config_vw

from flask import Flask


def create ():
	app = Flask(__name__.split('.')[0])
	
	# Configuração do db
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	
	# registra as configurações do SQLAchemy no app
	config_db(app)
	
	# registra as blueprints no app
	config_vw(app)
	
	return app
