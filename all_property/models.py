from django.db import models


class Property(models.Model):
    title = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50)
    purpose = models.CharField(
        max_length=10,
        choices=[
            ('sell', 'Sell'),
            ('rent', 'Rent'),
        ]
    )
    completion = models.CharField(
        max_length=20,
        choices=[
            ('all', 'All'),
            ('ready', 'Ready'),
            ('unready', 'Unready'),
            ('under_construction', 'Under Construction'),
        ]
    )
    status = models.CharField(
        max_length=10,
        choices=[
            ('booked', 'Booked'),
            ('available', 'Available'),
        ],
        default='available'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=255)

class Location(models.Model):
    division = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    thana_police_station = models.CharField(max_length=255)
    upazila = models.CharField(max_length=255)
    union_ward = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
