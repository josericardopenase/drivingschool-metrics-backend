# Generated by Django 4.2.3 on 2025-01-22 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrative_management', '0015_alter_registration_access_to_tests_expire_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='data_protection_file',
        ),
    ]
