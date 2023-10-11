from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, null=True, blank=True)
    contact_no = models.CharField(max_length=15, null=True, blank=True)
    area = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    district = models.CharField(max_length=30, null=True, blank=True)
    division = models.CharField(max_length=30, null=True, blank=True)
    parmanent_address = models.CharField(max_length=150, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_avatar = models.URLField(null=True, blank=True)

    def current_address(self):
        return f"{self.city}, {self.district}, {self.division}"

    def __str__(self):
        return str(self.user.username)
