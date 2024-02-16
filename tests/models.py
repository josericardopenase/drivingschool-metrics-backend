from django.db import models
from locations.models import Province
from drivingschools.models import DrivingPermission, DrivingSchoolSection
from queryable_properties.properties import queryable_property
from queryable_properties.managers import QueryablePropertiesManager
from django.db import models
from queryable_properties.managers import QueryablePropertiesManager
from django.db.models import Count, F, Value

# Create your models here.
class TestCenter(models.Model):
    name = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.name

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
    year= models.IntegerField()
    objects = QueryablePropertiesManager()

    @queryable_property(annotation_based=True)
    def num_suspensos(self):
        return F('num_presentados') - F('num_aptos')
    
    def __str__(self) -> str:
        return self.test_center.__str__() + " " + self.school_section.driving_school.__str__() + " " + "mes: " + self.month + " año" + self.year
