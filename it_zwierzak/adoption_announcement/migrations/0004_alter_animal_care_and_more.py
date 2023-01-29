# Generated by Django 4.0.6 on 2023-01-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoption_announcement', '0003_animal_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='care',
            field=models.TextField(blank=True, default=' ', max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='health_and_vaccination',
            field=models.TextField(blank=True, default=' ', max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='months',
            field=models.PositiveSmallIntegerField(default=0, help_text='fill when age is below 1 year'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='past',
            field=models.TextField(blank=True, default=' ', max_length=3000, null=True),
        ),
    ]
