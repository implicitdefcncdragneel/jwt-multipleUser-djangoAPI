# Generated by Django 3.2 on 2021-04-13 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userprofile',
            table='profile_teacher',
        ),
    ]
