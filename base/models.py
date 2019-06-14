from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class MyformData(models.Model):
    email2 = models.EmailField()
    first2 = models.CharField(max_length=30)
    last2 = models.CharField(max_length=30)
    published_date=models.DateTimeField(blank=True,null=True)
