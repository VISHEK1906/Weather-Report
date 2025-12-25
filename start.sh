#!/bin/sh
echo "-------------------------------------------"
echo "Your API is running at: http://127.0.0.1:8000/"
echo "-------------------------------------------"

python manage.py runserver --host 0.0.0.0 --port 8000
