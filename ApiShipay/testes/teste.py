from requests import get,post

class Teste():
	OK, FAIL = [],[]
	
	url = 'http://localhost:5000/api/v1/transacoes/'
	
	def get_status_estabelecimento(self):
		response = get(self.url+'?estabelecimento=45.283.163/0001-67')
		if response.status_code == 200:
			self.OK.append('get_status_estabelecimento')
		else:
			self.FAIL.append('get_status_estabelecimento')
			
			
	def get_status_estabelecimento_erro(self):
		
		response = get(self.url+'?estabelecimento=45.283.163/000')
		if response.status_code == 404:
			self.OK.append('get_status_estabelecimento_erro')
		else:
			self.FAIL.append('get_status_estabelecimento_erro')
	
	
	
	
	def post_nova_transacao_valida(self):
		dados_envio = {"estabelecimento":"45.283.163/0001-67","cliente": "094.214.930-01","valor": 591,"descricao": "Almoço em restaurante chique pago via Shipay!"}
		response = post(self.url,json=dados_envio)
		if response.status_code == 201:
			self.OK.append('post_nova_transacao_valida')
		else:
			self.FAIL.append('post_nova_transacao_valida')
	
	def post_nova_transacao_invalida(self):
		dados_envio = {"estabelecimento":"45.283.163/0001-67","cliente": "z","valor": 591,"descricao": "Almoço em restaurante chique pago via Shipay!"}
		response = post(self.url,json=dados_envio)
		if response.status_code == 206:
			self.OK.append('post_nova_transacao_invalida')
		else:
			self.FAIL.append('post_nova_transacao_invalida')


def init_test():
	test= Teste()
	test.get_status_estabelecimento()
	test.get_status_estabelecimento_erro()
	test.post_nova_transacao_invalida()
	test.post_nova_transacao_valida()
	
	print(f"""
------------------------------------------------
	\033[91mTestes que falharam: [{len(test.FAIL)}]\033[m
""")
	for item in test.FAIL:
		print(item)
	
	print(f"""
------------------------------------------------
	\033[92mTestes que Passaram: [{len(test.OK)}]\033[94m
""")
	for item in test.OK:
		print('\n'+item)

	print('\n\033[m\n')
init_test()