# Generated by Django 3.0.5 on 2020-04-07 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200404_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono'),
        ),
    ]
