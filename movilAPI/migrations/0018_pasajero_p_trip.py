# Generated by Django 4.1.3 on 2022-11-16 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movilAPI', '0017_remove_pasajero_p_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasajero',
            name='p_trip',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, related_name='p_trip', to='movilAPI.viaje'),
        ),
    ]