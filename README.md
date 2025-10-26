# ELEGSO Service (Django)

## Быстрый старт
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8001
