# LAB6

## Start project

mkdir lab6
cd lab6/
python -m venv env
source env/Scripts/Activate
pip install django
django-admin startproject myimgur
cd myimgur/
python manage.py startapp app
code .
winpty python manage.py runserver
