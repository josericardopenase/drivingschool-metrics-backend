from django.db import models

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name

class DrivingLicense(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

"""
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    taxes_included = models.BooleanField()
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class DrivingPractice(models.Model):
    license = models.ForeignKey(DrivingLicense, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    units = models.IntegerField()

    def __str__(self):
        return self.product.name


class CharField:
    pass
"""