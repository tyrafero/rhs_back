from django.shortcuts import render
from .models import FeaturedMenu

def index(request):
  featured_menus = FeaturedMenu.objects.all()  # Get all featured menus
  context = {'featured_menus': featured_menus}
  return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def reservation(request):
    return render(request, 'reservation.html')