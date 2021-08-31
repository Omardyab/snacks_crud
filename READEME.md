
# snacks_crud


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
    8-git remote add origin
    9-git push -u origin master
    6-django-admin startproject django_snacks .