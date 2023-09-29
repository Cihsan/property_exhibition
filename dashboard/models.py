from django.db import models
from accounts.models import Account

RATING = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))


# Create your models here.
class Favourites(models.Model):
    favourite_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    # property = models.ForeignKey(Property, on_delete=models.CASCADE)


class Testimonial(models.Model):
    testimonial_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    rating = models.IntegerField(choices=RATING, default=5)


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    # property = models.ForeignKey(Property, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
    total_amount = models.IntegerField()
    payment_status = models.CharField(
        max_length=9,
        choices=[("Pending", "Pending"), ("Completed", "Completed")],
        default="Pending",
    )
    created_at = models.DateTimeField(auto_now=True)
