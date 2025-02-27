from django.db import models

from business.models import Section


class EmployeeSoftware(models.Model):
    name = models.CharField(max_length=100, verbose_name="nombre")
    url = models.CharField(max_length=100, verbose_name="url")

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name="nombre")
    surname = models.CharField(max_length=100)
    birthday = models.DateField()
    DNI = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    personal_email = models.EmailField(max_length=100)

    is_active = models.BooleanField(default=True)
    check_in_date = models.DateField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)
    DNI_file = models.FileField(upload_to='docs/human_resources/', null=True, blank=True)
    declaration_data_protection = models.FileField(upload_to='docs/human_resources/', null=True, blank=True)
    declaration_no_sexual_offenses = models.FileField(upload_to='docs/human_resources/', null=True, blank=True)
    observations = models.TextField(verbose_name="observaciones", null=True, blank=True)
    is_teacher = models.BooleanField(default=False)
    is_administrative = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class EmployeeSoftwareAccount(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    software = models.ForeignKey(EmployeeSoftware, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, verbose_name="username")
    password = models.CharField(max_length=100, verbose_name="password")

    def __str__(self):
        return self.employee.name + " - " + self.software.name

class Teacher(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    teacher_degree = models.FileField(upload_to='docs/human_resources/', null=True, blank=True)
    teacher_authorization = models.FileField(upload_to='docs/human_resources/', null=True, blank=True)
    declaration_not_serving_sentence = models.FileField(upload_to='docs/human_resources/', null=True, blank=True)
    driving_license = models.FileField(upload_to='docs/human_resources/', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.employee.is_teacher = True
        self.employee.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.employee.name

class Administrative(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.employee.is_administrative = True
        self.employee.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.employee.name

class Contract(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    is_active = models.BooleanField(default=True)
    is_temporal = models.BooleanField(default=False)
    hours_a_week = models.IntegerField(default=0)
    file = models.FileField(upload_to='docs/human_resources/')

    def __str__(self):
        return '{} {} ({}h)'.format(self.employee.name, self.date.strftime("%d-%m-%Y"), self.hours_a_week)


class Payroll(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    file = models.FileField(upload_to='docs/human_resources/')

class Vacation(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    init_date = models.DateField()
    end_date = models.DateField()

class Absence(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    is_sick_leave = models.BooleanField(default=False)
    is_justified = models.BooleanField(default=False)
    init_date = models.DateField()
    end_date = models.DateField()
    hours = models.IntegerField(default=0)
    reason= models.TextField(verbose_name="Reason")
    justification = models.FileField(upload_to='docs/human_resources/')

    def __str__(self):
        return self.employee.name
