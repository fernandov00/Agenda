Começar projeto django

'''
python -m venv venv
venv/Scripts/activate
pip install django
django-admin startproject mysite . 
'''

configurando o git

'''
git config --global user.name "fernandov00"
git config --global user.email "dalmolinvieirafernando@gmail.com"

git config --global init.defaultBranch main

git init
git add.
git commit -m "primeiro commit"
'''

migrando a base de dados
'''
python manage.py makemigrations
python manage.py migrate
'''

criando super usuario django
'''
python manage.py createsuperuser
python manage.py changepassword USERNAME
'''

