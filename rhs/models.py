from django.db import models

class FeaturedMenu(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  image = models.ImageField(upload_to='featured_menus')  # Specify upload directory
  ingredients = models.CharField(max_length=255) 

from django.db import models

class MenuItem(models.Model):
    Entries = 'Entries'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    DRINKS = 'Drinks'
    DESSERT = 'Dessert'
    FeedMe = 'FeedMe'

    CATEGORY_CHOICES = [
        (Entries, 'Entries'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (DRINKS, 'Drinks'),
        (DESSERT, 'Dessert'),
        (FeedMe, 'FeedMe'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_special = models.BooleanField(default=False)
    is_special_front = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    num_people = models.IntegerField()
    specific_requirements = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='author_images', null=True, blank=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)