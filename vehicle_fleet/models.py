from django.db import models
from business.models import DrivingLicense


class FuelType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    image = models.FileField(upload_to='vehicles/')
    plate_number = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    driving_license = models.ForeignKey(DrivingLicense, on_delete=models.CASCADE)

    insurance_payment_date = models.DateField(null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)

    vehicle_circulation_permission_document = models.FileField(upload_to='docs/vehicles/', verbose_name="Permiso de circulacion", blank=True, null=True)
    technical_data_sheet_document = models.FileField(upload_to='docs/vehicles/', verbose_name="Ficha tecnica", blank=True, null=True)
    insurance_document = models.FileField(upload_to='docs/vehicles/', blank=True, null=True)
    itv_document = models.FileField(upload_to='docs/vehicles/', blank=True, null=True)


    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.plate_number


