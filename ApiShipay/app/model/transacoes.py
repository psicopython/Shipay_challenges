from flask import current_app as cp
from app.model import db

from datetime import datetime

from cryptography.fernet import Fernet 
KEY = b'algkmkJbj7iZOL-lFW_7Mm8uRRFPU9xK7wYPvrwOsfA='



class Transacoes(db.Model):
	
	__tablename__= 'recebimentos'
	
	id = db.Column(db.Integer, primary_key=True)
	valor = db.Column(db.Unicode, nullable=False)
	data  = db.Column(db.DateTime, nullable=False)
	descricao = db.Column(db.Text, nullable=False)
	cliente = db.Column(db.String(32), nullable=False)
	estab = db.Column(db.String(32),nullable=False)
	
	def _get_data(self):
		return datetime.now()
		
	def encrypt(self,arg):
		return Fernet(KEY).encrypt(bytes(arg,'utf8'))

	def decrypt(self,arg):
		return Fernet(KEY).decrypt(arg).decode('utf8')
	
	
	def __init__(self, cliente,valor, descricao, cnpj):
		
		self.data = self._get_data()
		self.estab = cnpj
		self.valor = self.encrypt(str(valor))
		self.cliente = cliente
		self.descricao = self.encrypt(descricao)
	
	def get_receb(self):
		return {
			"cliente": self.cliente ,
			"descricao": self.decrypt(self.descricao) ,
			"data": self.data.strftime("%d/%m/%y as %H:%M"),
			"valor": "R$"+str(self.decrypt(self.valor)) ,
		}






class Estabelecimento(db.Model):
	
	__tablename__ = 'estabelecimento'
	
	id = db.Column(db.Integer,primary_key=True)
	nome = db.Column(db.Unicode,nullable=False)
	dono = db.Column(db.Unicode,nullable=False)
	cnpj = db.Column(db.String(32),unique=True, nullable=False)
	telefone = db.Column(db.Unicode, nullable=False)
	
	
	def encrypt(self, arg):
		return Fernet(KEY).encrypt(bytes(arg,'utf-8'))
	
	def decrypt(self, arg):
		return Fernet(KEY).decrypt(arg).decode('utf-8')
	
	def __init__(self,nome, cnpj, dono, telefone):
		
		self.cnpj = cnpj
		self.nome = self.encrypt(nome)
		self.dono = self.encrypt(dono)
		self.telefone = self.encrypt(telefone)
	
	
	def get_estab(self):
		recebimentos = Transacoes.query.filter_by(estab=self.cnpj).limit(10)
		list_receb =[]
		total = 0.0
		for rec in  recebimentos:
			if recebimentos: 
				list_receb.append(rec.get_receb())
				total += float(rec.get_receb()['valor'].replace('R$',''))
		
		return {
			"estabelecimento": {
				"nome": self.decrypt(self.nome),
				"cnpj": self.cnpj,
				"dono": self.decrypt(self.dono),
				"telefone": self.decrypt(self.telefone),
			},
			"recebimentos": list_receb,
			"total": f'R${total:.2f}',
		}

def popular_db():
	
	nome = "Nosso Restaurante de Todo Dia LTDA"
	cnpj = "45.283.163/0001-67"
	dono = "Fabio I."
	telefone="11909000300"
	valor= 590.01
	cliente ="094.214.930-01"
	descricao = "Almoço em restaurante chique pago via Shipay!"
	
	estab = Estabelecimento(
		nome=nome,cnpj=cnpj,
		dono=dono, telefone=telefone,
	)
	
	
	receb = Transacoes(
		valor=valor, cliente=cliente,
		descricao=descricao, cnpj=cnpj,
	)
	cp.db.session.add_all([estab,receb])
	cp.db.session.commit()
	