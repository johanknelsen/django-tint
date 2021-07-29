import os

mysite = input('What is the site to be named?')
app = input('What is the app name?')
cwd = os.getcwd()

os.system(f'django-admin startproject {mysite}')


os.chdir(mysite)
os.system(f"python manage.py startapp {app}")
#os.chdir(cwd)


os.system('python manage.py migrate')

os.system(f'python manage.py makemigrations {app}')

os.system('python manage.py migrate')

os.system('python manage.py createsuperuser')

os.system('python manage.py runserver')

