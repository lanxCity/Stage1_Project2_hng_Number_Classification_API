#!/usr/bin/env python3
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput