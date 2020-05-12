# Generated by Django 3.0.5 on 2020-05-10 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0002_auto_20200510_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmenttype',
            name='name',
            field=models.CharField(choices=[('Casa', 'Casa'), ('Apartamento', 'Apartamento'), ('Piso', 'Piso'), ('Planta', 'Planta'), ('Habitacion', 'Habitacion')], max_length=100, verbose_name='Tipo de propiedad'),
        ),
    ]