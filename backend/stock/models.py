from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name_ch = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    category = models.CharField(max_length=10)
    ticker = models.CharField(max_length=10)
    stocktype = models.CharField(max_length=10)
    website = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)