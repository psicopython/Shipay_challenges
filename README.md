# Shipay_challenges

### Primeiro Desafio:

```sh
# no terminal
git clone github.com/psicopython/Shipay_challenges

cd Shipay_challenges

python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

cd ApiShipay

export FLASK_APP=app:create

flask db init
flask db migrate
flask db upgrade

flask shell

# no shell do flask
from app.model.transacoes import popular_db
popular_db()
exit()

# fora do flask shell 
flask run


# em outra janela do terminal 
cd ../testes
python testes.py

```

## Desafio 2

 Eu reestruturei o código, criei novos arquivos e 
 modularizei td o app, ele esta localizado em 
 Shipay_challenges/João/depois/