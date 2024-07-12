# this is the page that shows all items and data in the db

from django.contrib import admin
from .models import Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('meal', 'status')
    list_filter = ('status',)
    search_fields = ('meal', 'description')

# above lines will display all the fields shown from models.py

admin.site.register(Item, MenuItemAdmin)
# above line Item from models.py is coupled with MenuItemAdmin

# next a super user can be created using:

# python manage.py createsuperuser

# current user: tom password: pop
