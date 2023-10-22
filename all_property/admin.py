from django.contrib import admin

# Register your models here.
from .models import Property, Property_Images


# Register your models here.
admin.site.register(Property)
admin.site.register(Property_Images)
