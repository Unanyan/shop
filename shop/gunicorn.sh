#!/usr/bin/env sh

set -o errexit
set -o nounset

cd /code
#PGPASSWORD=postgres createdb -h db -U postgres donation_platform

python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --noinput
python manage.py compilemessages

python manage.py loaddata fixtures/initial1.json
# certs/privkey.pem certs/cert.pem
# Start gunicorn with 4 workers:
/usr/local/bin/gunicorn shop.wsgi -w 4 -b 0.0.0.0:8000 --chdir=./
# /usr/local/bin/gunicorn --certfile=cart.crt --keyfile=privkey.key donation_platform.wsgi -w 4 -b 0.0.0.0:8000 --chdir=./
