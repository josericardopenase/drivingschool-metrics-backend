# Generated by Django 4.2.3 on 2024-02-16 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivingschools', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TestCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='locations.province')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_aptos', models.IntegerField()),
                ('num_presentados', models.IntegerField()),
                ('num_aptos_1_conv', models.IntegerField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('permission_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='drivingschools.drivingpermission')),
                ('school_section', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='drivingschools.drivingschoolsection')),
                ('test_center', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tests.testcenter')),
                ('test_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tests.testtype')),
            ],
        ),
    ]
