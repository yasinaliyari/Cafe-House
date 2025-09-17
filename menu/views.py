from django.shortcuts import render
from menu.models import MenuItem


def menu_page(request):
    items = MenuItem.objects.filter(is_active=True)
    return render(request, "menu/menu.html", {"menu_items": items})
