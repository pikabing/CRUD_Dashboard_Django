# CRUD_Dashboard_Django

This is a admin panel/dashboard based on Django, MySQL. 
The dashboard has the functionality to create, delete, edit users.
We can also change a user's status from active to inactive.

How to run:
  
  1. Download/Clone this repo
  2. pip install django
  3. pip install bootstrap4
  4. python manage.py migrate
  5. python manage.py makemigrations users
  6. python manage.py runserver
  
I connected this dashboard to a local xampp server, which had a database (name is set in settings.py). You can alter/set the db accordingly.

** convention is to be followed - 
1. Table name should be: (app_name)_(model_name) - all in small 
2. Table column names are to be the same as in models.py
