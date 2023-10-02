from django.db import models
from accounts.models import Account
from all_property.models import Property

RATING = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

# Create your models here.


class Favourites(models.Model):
    favourite_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)


class Testimonial(models.Model):
    testimonial_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    rating = models.IntegerField(choices=RATING, default=5)

    class Meta:
        unique_together = ["user", "testimonial_id"]


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True)
    booking_date = models.DateTimeField()
    total_amount = models.IntegerField()
    payment_status = models.CharField(
        max_length=9,
        choices=[("Pending", "Pending"), ("Completed", "Completed")],
        default="Pending",
    )
    created_at = models.DateTimeField(auto_now=True)


class Promotion(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    promotion_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
