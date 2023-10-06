from django.contrib import admin
# Register your models here.
from .models import Property, PropertyImage

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title','type', 'price', 'area', 'purpose','completion','status','created_at', 'updated_at')
    list_filter = ('type', 'status', 'purpose')
    search_fields = ('title', 'description', 'type', 'purpose')



admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyImage,admin.ModelAdmin)