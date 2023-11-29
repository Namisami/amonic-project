# Generated by Django 4.2.6 on 2023-11-19 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_visit_login_time_visit_logout_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='login_time',
            field=models.DateTimeField(null=True, verbose_name='Время входа'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]