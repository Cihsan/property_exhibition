# Generated by Django 4.2.5 on 2023-10-11 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('contact_no', models.CharField(blank=True, max_length=15)),
                ('area', models.CharField(blank=True, max_length=30)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('district', models.CharField(blank=True, max_length=30)),
                ('division', models.CharField(blank=True, max_length=30)),
                ('parmanent_address', models.CharField(blank=True, max_length=150)),
                ('date_of_birth', models.DateField(blank=True)),
                ('profile_avatar', models.URLField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]