# Generated by Django 4.2.6 on 2023-11-08 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='aircraft',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='airports.aircraft', verbose_name='Самолет'),
        ),
    ]
