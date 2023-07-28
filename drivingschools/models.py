from django.db import models

class DrivingSchool(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{} {}".format(self.code, self.name)

class DrivingSchoolSection(models.Model):
    driving_school = models.ForeignKey(DrivingSchool, on_delete=models.CASCADE)
    code = models.IntegerField()

    def __str__(self):
        return "{} {}".format(self.driving_school, self.code)
    
class DrivingPermission(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name