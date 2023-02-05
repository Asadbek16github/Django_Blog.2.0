from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CostomUser(AbstractUser):
    age = models.PositiveIntegerField(null=False, blank=False)
    birthYear = models.PositiveIntegerField(null=False, blank=False)
    living_country = models.CharField(max_length=100, null=False, blank=False)
    living_city = models.CharField(max_length=100, null=False, blank=False)

