import imp
from operator import mod
from django.db import models
import django.core.validators as validators

# Create your models here.
class Confederation(models.Model):
  name = models.CharField(max_length=255)
  
  def __str__(self):
    return self.name


class Country(models.Model):
  full_name = models.CharField(max_length=255)
  fifa_code = models.CharField(max_length=3)
  flag_url = models.CharField(max_length=255)
  confederation = models.ForeignKey(Confederation, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.full_name




