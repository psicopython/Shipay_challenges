
# a função responsável pela rota
from .transacao import transacoes

from flask import Blueprint 

#instanciando a Blueprint
bp = Blueprint("api",__name__.split('.')[0],url_prefix='/api/v1/')

# criando uma rota simples para esta Blueprint
bp.add_url_rule(
	'/transacoes/',
	methods=["GET","POST"],
	view_func=transacoes,
	endpoint="transacoes"
)

# def que registava Blueprint
def config_vw(app):
	app.register_blueprint(bp)
	
