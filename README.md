# kachelin-backend
SPARCS Project

## START THE SERVER
```
source .venv/bin/activate
pip3 install -r requirements.txt
cp .env.example .env
Check the .env
python3 manage.py migrate
python3 manage.py runserver
```

## SPEC
- Django w/ REST FRAMEWORK
- Postgresql
- JWT
- REST-AUTH
- SWAGGER and Redoc