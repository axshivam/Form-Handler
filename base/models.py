from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class ClassName(models.Model):
    """docstring for ."""
    email2 = models.EmailField()
    first2 = models.CharField(max_length=30)
    last2 = models.CharField(max_length=30)
    published_date=models.DateTimeField(blank=True,null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        self.save()
