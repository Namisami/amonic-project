# Generated by Django 4.2.6 on 2023-10-28 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_last_logout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='office_id',
            new_name='office',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='role_id',
            new_name='role',
        ),
    ]
