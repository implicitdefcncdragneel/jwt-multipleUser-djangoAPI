# Generated by Django 3.2 on 2021-04-13 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('institute_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('whats_app', models.CharField(default=False, max_length=10)),
                ('city', models.CharField(default=False, max_length=50)),
                ('area', models.CharField(default=False, max_length=50)),
                ('pincode', models.PositiveIntegerField(default=False)),
                ('address', models.CharField(default=False, max_length=50)),
                ('class_type', models.CharField(default=False, max_length=50)),
                ('segment', models.CharField(default=False, max_length=50)),
                ('fees', models.CharField(default=False, max_length=50)),
                ('name', models.CharField(default=False, max_length=50)),
                ('dob', models.CharField(default=False, max_length=50)),
                ('communication_address', models.CharField(default=False, max_length=250)),
                ('pincode1', models.PositiveIntegerField(default=False)),
                ('phone_number1', models.CharField(max_length=10, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='institute', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile_institute',
            },
        ),
    ]
