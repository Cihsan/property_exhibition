# Generated by Django 4.2.5 on 2023-10-19 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='start_date',
            field=models.DateField(blank=True),
        ),
    ]
