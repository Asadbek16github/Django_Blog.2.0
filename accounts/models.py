from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CostomUsers(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    birthYear = models.PositiveIntegerField(null=True, blank=True)
    living_country = models.CharField(max_length=100, null=True, blank=True)
    living_city = models.CharField(max_length=100, null=True, blank=True)

