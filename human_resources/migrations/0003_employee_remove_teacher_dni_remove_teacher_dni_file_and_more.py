# Generated by Django 4.2.3 on 2024-12-12 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0002_teacher_check_in_date_teacher_check_out_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('surname', models.CharField(max_length=100)),
                ('DNI', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('personal_email', models.EmailField(max_length=100)),
                ('work_email', models.EmailField(max_length=100)),
                ('work_email_password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField(blank=True, null=True)),
                ('DNI_file', models.FileField(upload_to='human_resources/')),
                ('declaration_data_protection', models.FileField(upload_to='human_resources/')),
                ('declaration_no_sexual_offenses', models.FileField(upload_to='human_resources/')),
            ],
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='DNI',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='DNI_file',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='check_in_date',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='check_out_date',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='declaration_data_protection',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='declaration_no_sexual_offenses',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='personal_email',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='work_email',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='work_email_password',
        ),
        migrations.AddField(
            model_name='teacher',
            name='employee',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='human_resources.employee'),
            preserve_default=False,
        ),
    ]
