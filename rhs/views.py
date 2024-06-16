from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from datetime import datetime
from django.contrib import messages  # Import messages framework
from django.urls import reverse
from .models import MenuItem, Post
from django import forms



def index(request):
  menu_items = MenuItem.objects.filter(is_special=True)
  posts = Post.objects.all()
  context = {'menu_items': menu_items,'posts': posts}
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
    categories = ["Entries", "Lunch", "Dinner","Drinks", "Dessert", "FeedMe"]
    menu_data = []
    
    for category in categories:
        items = MenuItem.objects.filter(category=category)
        print(f"Category: {category}, Items: {items}")  # Debug print to check fetched items
        menu_data.append((category, items))
    
    return render(request, 'menu.html', {'menu_data': menu_data})

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'  # Include all fields from the model

def manage_menu(request, menu_item_id=None):
    """
    Handles both adding and editing menu items.
    """
    if menu_item_id:  # Editing an existing item
        menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
        if request.method == 'POST':
            form = MenuItemForm(request.POST, request.FILES, instance=menu_item)
            if form.is_valid():
                form.save()
                return redirect(reverse('manage_menu'))  # Redirect to the manage page
        else:
            form = MenuItemForm(instance=menu_item)
    else:  # Adding a new item
        if request.method == 'POST':
            form = MenuItemForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect(reverse('manage_menu'))  # Redirect to the manage page
        else:
            form = MenuItemForm()
    
    menu_items = MenuItem.objects.all()
    return render(request, 'add_menu.html', {'form': form, 'menu_items': menu_items})

def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu_list.html', {'menu_items': menu_items})

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog-single.html')



from django.core.mail import send_mail
from django.conf import settings


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'  # Include all fields from the Reservation model
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Use HTML5 date input
            'time': forms.TimeInput(attrs={'type': 'time'}),  # Use HTML5 time input
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date and time:
            try:
                date_time = datetime.combine(date, time)
                cleaned_data['date_time'] = date_time
            except ValueError:
                raise forms.ValidationError("Invalid date or time format")
        return cleaned_data

def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()  # Save the reservation object and get the Reservation object

            # Send email confirmation
            subject = 'Your Reservation Confirmation'
            message = f'Thank you for your reservation! Your reservation details are:\n\n' \
                      f'Date: {reservation.date}\n'\
                      f'Time: {reservation.time}\n'\
                      f'Name: {reservation.name}\n'\
                      f'Email: {reservation.email}\n'\
                      f'Phone: {reservation.phone}\n'\
                      f'Number of People: {reservation.num_people}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [reservation.email]
            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, 'Your reservation has been successfully booked!')
            print('Your reservation has been successfully booked!')
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})

def blog(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
        'author': post.author,
        'tags': post.tags.all()
    }
    return render(request, 'blog-single.html', context)

from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact.save()
        messages.success(request, 'Your message has been sent successfully.')
        return redirect('contact')

    return render(request, 'contact.html')