# Generated by Django 4.2.3 on 2024-12-12 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0006_alter_teacher_driving_license'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeSoftware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('url', models.CharField(max_length=100, verbose_name='url')),
            ],
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='control_l_password',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='control_l_user',
        ),
        migrations.CreateModel(
            name='EmployeeAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='username')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resources.employee')),
                ('software', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resources.employeesoftware')),
            ],
        ),
        migrations.CreateModel(
            name='Administrative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='human_resources.employee')),
            ],
        ),
    ]
