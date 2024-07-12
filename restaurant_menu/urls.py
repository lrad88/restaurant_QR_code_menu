
from django.urls import path

from . import views

"""urls.py in restaurant_menu folder is where you connect the 
classes in views.py to the front end and make them visible """

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    # menulist is the class in views.py and is the front page of the
    # website as_view() renders this class as an actual view, with
    # function based views this isn't necessary
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name='menu_item'),
    # int:pk is used to handle dynamic urls and without it you will get
    # an attribute error when loading the page asking for an object pk
    # 'primary key' from the database which is simply a row number in
    # the database, a 'row.pk' needs to be added to the index.html
    # otherways another error will occur

]

# from here you have to go to urls.py in my site to register your app path

