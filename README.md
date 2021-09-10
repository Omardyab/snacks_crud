# snacks_crud

PR:https://github.com/Omardyab/snacks_crud/pull/2

# Getting Run 

    1-poetry init -n
    2-poetry add django
    3-poetry add --dev black flake8
    4-add .gitignore including:
        *.log
        *.pot
        *.pyc
        __pycache__/
        local_settings.py
        db.sqlite3
        db.sqlite3-journal
        media
    all from here: https://www.toptal.com/developers/gitignore/api/django
    5-poetry shell
    6-git init
    7-git add .
    git commit -m "first commit"
    8-git remote add origin sshurl
    9-git push -u origin master
    6-django-admin startproject django_snacks . //check poetry shell is activated
    python manage.py migrate
    python manage.py runserver 
    now your app would show "The install worked successfully! Congratulations!" 
    python manage.py startapp snacks_crud
    python manage.py createsuperuser
    
