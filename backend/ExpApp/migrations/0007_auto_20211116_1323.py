# Generated by Django 3.2.6 on 2021-11-16 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExpApp', '0006_auto_20211115_0806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='city',
            new_name='city_name',
        ),
        migrations.RenameField(
            model_name='district',
            old_name='district',
            new_name='district_name',
        ),
    ]
