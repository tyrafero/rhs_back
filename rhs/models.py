from django.db import models

class FeaturedMenu(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  image = models.ImageField(upload_to='featured_menus')  # Specify upload directory
  ingredients = models.CharField(max_length=255) 