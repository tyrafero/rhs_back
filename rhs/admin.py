from django.contrib import admin
from .models import FeaturedMenu, MenuItem, Reservation, Post, Author, Tag
# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'num_people')

admin.site.register(FeaturedMenu)
admin.site.register(MenuItem)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)