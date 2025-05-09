# Generated by Django 5.1.4 on 2025-02-11 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('resident_type', models.CharField(choices=[('owner', 'Owner'), ('tenant', 'Tenant')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('gps_latitude', models.FloatField()),
                ('gps_longitude', models.FloatField()),
                ('rent_status', models.BooleanField(default=False)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('remarks', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
    ]
