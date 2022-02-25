# IMS - Inventory Management System
Application used for managing the hardware tool inventory (API included)

# Django framework
## Setup
- pip install django
- django-admin startproject ims .
- python manage.py startapp tools
- python manage.py runserver 8080

## Project structure
- model view template architecture
- a project contains multiple apps
- tools is an app

tools app structure:
- admin - how the administration area would look like
- apps - store various configurations for this app
- models - classes that represent the app data
- tests - automate tests
- views - contains view functions (function that takes a request and return a response)
- urls - url configuration

## Migration
- register the app in settings.py
- python manage.py makemigrations 
- python manage.py migrate

## Admin
python manage.py createsuperuser

## API
pipenv install django-tastypie

## Heroku Deployment:
### Prepare for deployment:
- Install heroku CLI and git.
- Install gunicorn webserver: pip install gunicorn
- create Procfile
- Prepare static files for deployment: create static folder and declare it inside settings (STATIC_ROOT)
- python manage.py collectstatic
- pip install whitenoise
- add whitenoise to settings (MIDDLEWARE)

### Deploy application
- pip freeze > requirements.txt
- Go to settings and update ALLOWED_HOSTS.
- Push code
```
git init
git add .
git commit -m "Inital commit"
heroku login
heroku create
git push heroku master
```
