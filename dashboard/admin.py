from django.contrib import admin
from .models import Promotion, Favourites, Testimonial, Booking


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("booking_id", "user", "property", "created_at")

    def created_at(self, obj):
        return obj.created.strftime("%Y-%m-%d %H:%M:%S")

    created_at.short_description = "Created At"


admin.site.register(Promotion)
admin.site.register(Favourites)
admin.site.register(Testimonial)
