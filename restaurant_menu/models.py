"""

GETTING STARTED

1-pip install django

2-django-admin startproject mysite . - creates a mysite folder
with all the Django files

3-python manage.py startapp restaurant_menu - creates another directory

4-In mysite / settings.py - installed_apps - include ‘restaurant_menu’,

5-python manage.py runserver - starts the django server

6-restaurant_menu / models.py is where you will create the db table

7-once the table is created type python manage.py makemigrations
which will create a migrations file

8-python manage.py migrate which will apply the migrations
in 0001_initial.py. a database file has now been created, containing
the auth_user and restaurant_menu_item tables

9 - next step is to go to views.py and follow the pages

10 - next you can run the server with python manage.py runserver

11- make sure to register the site in admin.py and create a superuser
and you will be able to http://127.0.0.1:8000/admin

12-next after populating your item list in the admin area
its time to display these items on the front page from index.html

"""

from django.db import models
from django.contrib.auth.models import User
import PIL

# user is a database that contains the username and password
# of different users


MEAL_TYPE = (
    ("starters", "Starters"), ("salads", "Salads"),
    ("main_dishes", "Main_Dishes"), ("desserts", "Desserts")
)

STATUS = (
    (0, "Unavailable"), (1, "Available")
)


# database columns
class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    # unique protects the table from having duplicates
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    # choice creates a drop-down menu
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    # above line allows for there to be multiple users that can add
    # items to the menu
    # on_delete=models.CASCADE means that when the user is deleted
    # all their items will be deleted as well
    # models.PROTECT prevents the deletion of the users items if the
    # user is deleted
    # models.SET_NULL will set the user to null if they are deleted and
    # will keep the items
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    # above generates a timestamp for when a user adds an item
    date_updated = models.DateTimeField(auto_now=True)
    # above records when an item is updated or edited
    image = models.ImageField(upload_to="static/images", null=True, blank=True)

    def __str__(self):
        return self.meal
    # above whenever an item is printed, it will
    # show the name of the item

