#!/bin/bash

NAME="{{cookiecutter.app_name}}"
DJANGODIR={{cookiecutter.project_root}}
USER=uehara1414
GROUP=uehara1414
NUM_WORKERS=1
DJANGO_SETTINGS_MODULE={{cookiecutter.project_name}}.settings
DJANGO_WSGI_MODULE={{cookiecutter.project_name}}.wsgi

echo "Starting $NAME as `whoami`"

cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

pipenv run gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=0.0.0.0:{{cookiecutter.port}}
