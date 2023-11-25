#!/bin/bash

sleep 10s
python manage.py migrate --noinput
python manage.py collectstatic --no-input
gunicorn config.wsgi:application --bind 0.0.0.0:8000  --reload