# Generated by Django 4.2.3 on 2023-07-22 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrivingSchool',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DrivingSchoolSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('driving_school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivingschools.drivingschool')),
            ],
        ),
    ]