# Django Auth with Firebase
![](https://img.shields.io/badge/django-3.1.3-blue?style=flat-square&logo=django)
[![](https://img.shields.io/badge/website-heroku-blueviolet?style=flat-square&logo=heroku)](https://twf-flours-task.herokuapp.com/)


A django web app with firebase authentication for users
 # Installation

 ## Prerequsites
 - Python 
 - Django
 - Pyrebase

 ## How to set up locally
- Fork and clone repo on your machine.
    ```
    git clone https://github.com/ExpressHermes/Firebase-Auth-Django.git
    ```

- Create a virtual environment. Activate it. Make sure it is in the same directory as the cloned repo.

    ```
    # for linux users
    python -m venv env
    source env/bin/activate 
    ```
- Install all requirements.
    ```
    pip install -r requirements.txt
    ```
- Inside the project folder, create migrations 
    ```
    python manage.py migrate
    ```
- Run the project with `local_settings`
    ```
    python manage.py runserver --settings=main.local_settings
    ```
