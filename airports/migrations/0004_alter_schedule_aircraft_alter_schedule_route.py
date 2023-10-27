# Generated by Django 4.2.6 on 2023-10-27 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0003_cabintype_alter_airport_country_alter_office_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='aircraft',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='airports.aircraft', verbose_name='Самолет'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='airports.route', verbose_name='Рейс'),
        ),
    ]
