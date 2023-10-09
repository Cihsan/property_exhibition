# Generated by Django 4.2.5 on 2023-10-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_property', '0002_property_img_url_alter_property_completion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='property_type',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='property',
            name='completion',
            field=models.CharField(choices=[('All', 'All'), ('Ready', 'Ready'), ('Incomplete', 'Incomplete'), ('Under Construction', 'Under Construction')], max_length=30),
        ),
        migrations.AlterField(
            model_name='property',
            name='purpose',
            field=models.CharField(choices=[('Sell', 'Sell'), ('Rent', 'Rent')], max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('Booked', 'Booked'), ('Available', 'Available')], default='Available', max_length=10),
        ),
    ]
