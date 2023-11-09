# Generated by Django 4.2.6 on 2023-11-08 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0003_alter_airport_country_alter_airport_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='business_seats',
            field=models.PositiveIntegerField(null=True, verbose_name='Мест в бизнес-классе'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='economy_seats',
            field=models.PositiveIntegerField(null=True, verbose_name='Мест в экономе'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='make_model',
            field=models.CharField(blank=True, max_length=255, verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='total_seats',
            field=models.PositiveIntegerField(null=True, verbose_name='Количество сидений'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='aircraft',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='airports.aircraft', verbose_name='Самолет'),
        ),
    ]
