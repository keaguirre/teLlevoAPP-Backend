# Generated by Django 4.1.3 on 2022-11-16 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movilAPI', '0022_alter_pasajero_p_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='v_state',
            field=models.CharField(default='Noiniciado', max_length=30, verbose_name='Estado'),
        ),
    ]