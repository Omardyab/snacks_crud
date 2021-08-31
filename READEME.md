

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
6-git add .
6-django-admin startproject django_snacks .