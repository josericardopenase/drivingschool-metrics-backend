from django.db import models
from django.db.models.signals import post_save

from administrative_management.models.student import Student
from business.models import DrivingLicense, Section
from django.dispatch import receiver
from datetime import timedelta
from django.utils.timezone import now

class RegistrationState(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    set_pasive_true = models.BooleanField(default=False)
    set_theorical_true = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Estado de la matrícula"
        verbose_name_plural = "Estados de la matrícula"

    def __str__(self):
        return self.name



class Registration(models.Model):
    registration_date = models.DateField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    license = models.ForeignKey(DrivingLicense, on_delete=models.CASCADE)
    #data_protection_file = models.FileField(upload_to='docs/data_protection')
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    states_log = models.ManyToManyField(
        RegistrationState,
        through='administrative_management.RegistrationStateLog',
        related_name='registrations'
    )


    access_to_tests_expire_date = models.DateField(auto_now_add=True)
    has_theorical_exam_pass = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.student.name + " " + self.license.name

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"



class RegistrationStateLog(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    state = models.ForeignKey(RegistrationState, on_delete=models.CASCADE, null=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Log de Estado"
        verbose_name_plural = "Logs de Estado"

    def __str__(self):
        return f"{self.registration} - {self.state} - {self.date_added}"

class TheoryAppRenovations(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

class MedicalCertificate(models.Model):
    code = models.CharField(max_length=100)
    expedition_date = models.DateField()
    has_glasses = models.BooleanField()
    has_limited_validation = models.BooleanField()
    has_restricted_conditions = models.BooleanField()
    medical_certificate_file = models.FileField(upload_to='students/')
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='medical_certificates')

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set expire date on the first save
            self.access_to_tests_expire_date = now().date() + timedelta(days=6*30)  # Approx. 6 months
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Certificado médico"
        verbose_name_plural = "Certificados médicos"

@receiver(post_save, sender=RegistrationStateLog)
def handle_registration_state_changes(sender, instance, **kwargs):
    registration = instance.registration
    state = instance.state

    if state.set_pasive_true and registration.is_active:
        registration.is_active = False

    if state.set_theorical_true and not registration.has_theorical_exam_pass:
        registration.has_theorical_exam_pass = True

    # Save the registration if any changes were made
    if registration.is_active is False or registration.has_theorical_exam_pass is True:
        registration.save()

@receiver(post_save, sender=TheoryAppRenovations)
def update_registration_expiry_date(sender, instance, created, **kwargs):
    if created:
        registration = instance.registration
        registration.access_to_tests_expire_date = now().date() + timedelta(days=6*30)  # Approx. 6 months
        registration.save()