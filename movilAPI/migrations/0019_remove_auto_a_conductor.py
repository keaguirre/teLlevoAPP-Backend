# Generated by Django 4.1.3 on 2022-11-16 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movilAPI', '0018_pasajero_p_trip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='a_conductor',
        ),
    ]