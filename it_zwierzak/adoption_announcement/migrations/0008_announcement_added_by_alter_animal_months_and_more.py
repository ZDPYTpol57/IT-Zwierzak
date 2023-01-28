# Generated by Django 4.0.6 on 2023-01-25 17:42

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adoption_announcement', '0007_announcement_delete_announcment'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='added_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='animal',
            name='months',
            field=models.PositiveSmallIntegerField(blank=True, default=0, help_text='fill when age is below 1 year', null=True, validators=[django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='animal',
            name='weight',
            field=models.FloatField(help_text='w kilogramach', max_length=10, validators=[django.core.validators.MinValueValidator(0.1)]),
        ),
    ]