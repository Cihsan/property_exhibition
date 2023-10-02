from django.contrib import admin
# Register your models here.
from .models import Property,Location, PropertyImage

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title','type', 'price', 'area', 'purpose','completion','status','created_at', 'updated_at')
    list_filter = ('type', 'status', 'purpose')
    search_fields = ('title', 'description', 'type', 'purpose')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('division','district', 'thana_police_station', 'upazila', 'union_ward','village')

admin.site.register(Property, PropertyAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(PropertyImage,admin.ModelAdmin)