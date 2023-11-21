# Generated by Django 4.2.6 on 2023-11-16 23:18

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 16, 23, 18, 47, 658605, tzinfo=datetime.timezone.utc), verbose_name='Время входа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visit',
            name='logout_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время входа'),
            preserve_default=False,
        ),
    ]
