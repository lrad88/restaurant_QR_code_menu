from django.shortcuts import render
# the last project used function based views, this project will
# use class based views which are less code heavy

from django.views import generic
# generic is a module that contains class based views

from .models import Item, MEAL_TYPE


class MenuList(generic.ListView):
    # variable names in the MenuList class need to have specific names
    # predefined by django eg. queryset, template_name
    # list view is good for displaying a list of objects or links
    queryset = Item.objects.order_by("-date_created")
    # above value will store the list of objects, order_by will
    # sort the objects based on the date_created variable from models.py
    template_name = "index.html"

    # This MenuList will be returned to the above template_name in the
    # templates folder

    # the above menu list view has to be connected to urls.py to be seen

    def get_context_data(self, **kwargs):
        #context = {"meals": ["Pizza", "Spaghetti", "Pasta"],
        #           "ingredients": ["Meat", "Potatoes", "Tomatoes"]}
        # context is a dictionary that will be passed to index.html
        # using the key "meals", above is an example of a static method
        # to display the options
        context = super().get_context_data(**kwargs)
        # above line gets the context data from the definition
        context["meals"] = MEAL_TYPE
        # meal_type taken from models.py, this almost must be imported,
        # it is a key for a dictionary, from here this can be displayed
        # through index.html

        return context


class MenuItemDetail(generic.DetailView):
    # MenuItemDetail is the same as MenuList and has specific class names
    model = Item
    # model = item refers to Item class in models.py, now you can refer to
    # models.py item class in the menu_item_detail.html
    template_name = "menu_item_detail.html"
    # This MenuItemDetail will be returned to the above template_name in
    # the templates folder
    # menuitemdetail is where your browser will go when you click on a
    # menu item

    pass
