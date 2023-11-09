# Generated by Django 4.2.6 on 2023-11-08 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_office_country'),
        ('airports', '0002_alter_schedule_aircraft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.country', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='airport',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Название'),
        ),
    ]
