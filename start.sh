#!/bin/sh
echo "-------------------------------------------"
echo "Your API is running at: http://127.0.0.1:8000/"
echo "-------------------------------------------"

python manage.py runserver 0.0.0.0:8000
