## Como Rodar o Projeto

### Console:
## Obs: realizar procedimento dentro da pasta pelo terminal cmd ou IDE.

pip install virtualenv

python -m venv .venv

.venv\scripts\activate

pip install -r requirements.txt

cp contrib/env-sample .env

docker-compose --build

docker-compose up | docker-compose up -d

python manage.py makemigrations  (opcional)

python manage.py createsuperuser

python manage.py migrate

python manage.py runserver

## * caso de erro verificar o USER= PASSWORD= no arquivo .env e inserir as informações de acordo com a sua configuração padrão do postgres
