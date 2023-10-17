from django.contrib import admin
from .models import Promotion, Favourites, Testimonial, Booking


# Register your models here.
admin.site.register(Booking)
admin.site.register(Promotion)
admin.site.register(Favourites)
admin.site.register(Testimonial)
