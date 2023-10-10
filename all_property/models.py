from django.db import models


class Property(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50)
    purpose = models.CharField(max_length=10, default="Sell")
    completion = models.CharField(max_length=30, default="Ready")
    status = models.CharField(
        max_length=10,
        default="Available",
    )
    division = models.CharField(max_length=80, null=True)
    district = models.CharField(max_length=50, null=True)
    upozila = models.CharField(max_length=50, null=True)
    img_url = models.URLField(max_length=300, null=True)
    union_ward = models.CharField(max_length=50, null=True)
    village = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def address(self):
        return f"{self.district}, {self.division}"
