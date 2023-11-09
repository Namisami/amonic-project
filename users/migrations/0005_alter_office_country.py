# Generated by Django 4.2.6 on 2023-11-08 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_office_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.country', verbose_name='Страна'),
        ),
    ]
