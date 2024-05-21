from django.shortcuts import render
from .models import FeaturedMenu

def index(request):
  featured_menus = FeaturedMenu.objects.all()  # Get all featured menus
  context = {'featured_menus': featured_menus}
  return render(request, 'index.html', context)

from .models import MenuItem

def menu_list(request):
    menu_items = MenuItem.objects.all()
    context = {'menu_list': menu_items}
    return render(request, 'menu/menu_list.html', context)

def special_menu_list(request):
    special_items = MenuItem.objects.filter(is_special=True)
    context = {'menu_list': special_items}
    return render(request, 'menu/menu_list.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    categories = ["Breakfast", "Lunch", "Dinner", "Dessert", "Wine"]
    menu_data = []
    
    for category in categories:
        items = MenuItem.objects.filter(category=category)
        print(f"Category: {category}, Items: {items}")  # Debug print to check fetched items
        menu_data.append((category, items))
    
    return render(request, 'menu.html', {'menu_data': menu_data})

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def reservation(request):
    return render(request, 'reservation.html')