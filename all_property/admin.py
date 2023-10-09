from django.contrib import admin

# Register your models here.
from .models import Property, PropertyImage


# Register your models here.
admin.register(Property)
admin.register(PropertyImage)
