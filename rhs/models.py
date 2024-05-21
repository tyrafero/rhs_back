from django.db import models

class FeaturedMenu(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  image = models.ImageField(upload_to='featured_menus')  # Specify upload directory
  ingredients = models.CharField(max_length=255) 

from django.db import models

class MenuItem(models.Model):
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    DRINKS = 'Drinks'
    DESSERT = 'Dessert'
    WINE = 'Wine'

    CATEGORY_CHOICES = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (DRINKS, 'Drinks'),
        (DESSERT, 'Dessert'),
        (WINE, 'Wine'),
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

