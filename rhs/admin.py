from django.contrib import admin
from .models import FeaturedMenu, MenuItem, Reservation
# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'num_people')

admin.site.register(FeaturedMenu)
admin.site.register(MenuItem)
admin.site.register(Reservation, ReservationAdmin)
