from django.db import models

# Create your models here.
class Coupons(models.Model):
    code = models.CharField(max_length=20)
    discout = models.IntegerField()

    def __str__(self):
        return self.code