from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Idioma"
        verbose_name_plural = "Idiomas"

class LeadSource(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Como nos conociste"
        verbose_name_plural = "Como nos conociste"

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    dni = models.CharField(max_length=100)
    dni_expire_date = models.DateField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    # ESTO PUEDE SER MUCHAS COSAS: provincia, municipio poblacion codigo postal calle nombre de la via numero bloque numero portal planta(planta baja 0) puerta escalera kilometro
    profile_picture = models.ImageField(upload_to='docs/profile_pictures')
    address = models.CharField(max_length=100)
    dni_file = models.FileField(upload_to='students/')
    acquisition_method = models.ForeignKey(LeadSource, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return '{self.name} {self.surname}'.format(self=self)

