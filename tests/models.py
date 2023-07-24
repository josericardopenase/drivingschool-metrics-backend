from django.db import models
from locations.models import Province
from drivingschools.models import DrivingPermission, DrivingSchoolSection

# Create your models here.
class TestCenter(models.Model):
    name = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.RESTRICT)

class TestType(models.Model):
    name = models.CharField(max_length=255)

class Test(models.Model):
    test_center = models.ForeignKey(TestCenter, on_delete=models.RESTRICT)
    test_type = models.ForeignKey(TestType, on_delete=models.RESTRICT)
    permission_type = models.ForeignKey(DrivingPermission, on_delete=models.RESTRICT)
    school_section = models.ForeignKey(DrivingSchoolSection, on_delete=models.RESTRICT)
    num_aptos = models.IntegerField()
    num_presentados = models.IntegerField()
    num_aptos_1_conv = models.IntegerField();
    month = models.IntegerField()
    year =models.IntegerField()

    @property
    def num_suspensos(self):
        return self.num_presentados - self.num_aptos
