
# tables
from app.model.transacoes import (
	Transacoes, Estabelecimento
)

# modulo, pacotes, classes e métodos
from flask import (
	request, jsonify,
	current_app, abort,
)


#func principal
def transacoes():
	if request.method == "POST":
		data = request.json
		
		cliente = data["cliente"]
		desc = data["descricao"]
		estab = data["estabelecimento"]
		valor = data["valor"]
		
		# valida o cpf
		cliente = val_cpf(cliente)
		
		#valida se existe este cnpj em nossos bancos de dados
		estab = val_cnpj(estab)
		
		# valida se é uma valor 'valido'
		valor = val_valor(valor)
		
		# if tudo estiver de acordo, adiciona ao banco de dados
		if cliente and desc and estab and valor:
			nova_transac = Transacoes(
					cliente=cliente,
					descricao=desc,
					cnpj=estab,
					valor=valor,
				)
			current_app.db.session.add(nova_transac)
			current_app.db.session.commit()
			
			# e por fim, retorna True
			return jsonify({'aceito': True}), 201
		# caso haja algo irregular
		else:
			# retorna False
			# 206 é conteudo parcial
			return jsonify({'aceito': False}), 206
			
		
	# if for uma requisição do tipo get
	elif request.method == 'GET':
		# pega o argumento
		dados = request.args.get('estabelecimento')
		# valida o argumento
		if val_cnpj(dados):
			# tenta pegar o cnpj correspondente
			estab = Estabelecimento.query.filter_by(cnpj=dados).first()
			# se tiver encontrado
			if estab:
				# retorna a função que o serializa
				return jsonify(estab.get_estab()), 200
			else:
				return jsonify({"erro_404":"Estabelecimento não encontrado"}),404
		else:
			return jsonify({"erro_404":"Cnpj Inválido"}),404
	else:
		# uso 404 como padrão por questão de segurança
		return abort(400,"foi mal brother, não achei oq vc estava procurando")
	


def val_valor(valor):
	""" validação simples só pra não passar despercebido¹"""
	try:
		if isinstance(valor,float):
			return float(valor)
		elif isinstance(valor,int):
			return float(valor)
		else:
			return False
	except Exception as e:
		return False
	

def val_cpf(cpf):
	""" validação simples só pra não passar despercebido²"""
	cpf_val = ''
	for item in list(cpf):
		if str(item).isdigit():
			cpf_val += item
	if len(cpf_val) == 11:
		return cpf

	

def val_cnpj(cnpj):
	""" validação simples só pra não passar despercebido³"""
	cnpj_val = ''
	for item in list(cnpj):
		if str(item).isdigit():
			cnpj_val += item
	if len(cnpj_val) == 14:
		return cnpj
	