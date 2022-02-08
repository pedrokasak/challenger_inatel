## Como Rodar o Projeto

### Console:
## Obs: realizar procedimento dentro da pasta pelo terminal cmd ou IDE.

pip install virtualenv

python -m venv .venv

.venv\scripts\activate


## (opcional) cp contrib/env-sample .env

docker-compose --build

docker-compose up | docker-compose up -d


## Para criar um super usuário

docker-compose stop
docker-compose up | docker-compose up -d
python manage.py createsuperuser

python manage.py migrate


## * caso de erro verificar o USER= PASSWORD=  e o 'HOST': 'db', no arquivo .env e inserir as informações de acordo com a sua configuração padrão do postgres
