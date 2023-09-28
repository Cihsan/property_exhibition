# Generated by Django 4.2.5 on 2023-09-28 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_first_name_user_name_remove_user_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=14)),
                ('address', models.TextField(max_length=50)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_pics/')),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]