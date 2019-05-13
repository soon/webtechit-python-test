from collections import namedtuple

from django.urls import reverse


MenuItem = namedtuple('MenuItem', ['name', 'url', 'icon', 'active'])


def make_menu_item(request, name, url, icon):
    return MenuItem(name, url, icon, request.path == url)


def menu(request):
    return {
        'menu_items': [
            make_menu_item(request, 'Home', reverse('home'), 'fas fa-home'),
            make_menu_item(request, 'Clients', reverse('clients:index'), 'fas fa-address-book'),
            make_menu_item(request, 'New Client', reverse('clients:create'), 'fas fa-user-plus'),
        ]
    }
