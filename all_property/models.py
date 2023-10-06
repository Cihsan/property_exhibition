from django.db import models
from .bdlocation import location


class Property(models.Model):
    title = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    property_type = models.CharField(
        max_length=50
    )  # Renamed 'type' to 'property_type' to avoid conflicts with Python reserved word
    purpose = models.CharField(
        max_length=10,
        choices=[
            ("sell", "Sell"),
            ("rent", "Rent"),
        ],
    )
    completion = models.CharField(
        max_length=30,
        choices=[
            ("all", "All"),
            ("ready", "Ready"),
            ("unready", "Unready"),
            ("under_construction", "Under Construction"),
        ],
    )
    status = models.CharField(
        max_length=10,
        choices=[
            ("booked", "Booked"),
            ("available", "Available"),
        ],
        default="available",
    )
    division = models.CharField(max_length=80, choices=location.Division, null=True)
    district = models.CharField(max_length=50, choices=location.District, null=True)
    upozila = models.CharField(max_length=50, choices=location.Upozila, null=True)
    union_ward = models.CharField(max_length=50, null=True)
    village = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="property/", default=None)

    def __str__(self):
        return self.property.title
