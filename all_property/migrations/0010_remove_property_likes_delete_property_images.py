# Generated by Django 4.2.5 on 2023-10-25 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all_property', '0009_alter_property_image1_alter_property_image2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Property_Images',
        ),
    ]
