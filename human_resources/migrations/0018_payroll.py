# Generated by Django 4.2.3 on 2025-01-16 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0017_remove_contract_name_contract_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='human_resources.employee')),
            ],
        ),
    ]
