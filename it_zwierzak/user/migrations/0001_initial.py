# Generated by Django 4.0.6 on 2023-01-29 10:22

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=17)),
                ('street', models.CharField(max_length=16)),
                ('house_number', models.CharField(max_length=6)),
                ('apartment_number', models.CharField(max_length=6)),
                ('postcode', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=16)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
