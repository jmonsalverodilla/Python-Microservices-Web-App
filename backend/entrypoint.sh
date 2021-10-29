#!/bin/bash
flask db init
flask db migrate
flask db upgrade
#python create_app.py db init
#python create_app.py db migrate
#python create_app.py db upgrade
gunicorn --bind 0.0.0.0:$BACKEND_PORT main:app