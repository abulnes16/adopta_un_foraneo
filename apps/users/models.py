from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name='Rol'
        verbose_name_plural='Roles'

    def __str__(self):
        return self.description


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='Rol')
    name = models.CharField('Nombres', max_length=200)
    last_name = models.CharField('Apellidos', max_length=200, blank=True, null=True)
    email = models.EmailField('Correo')
    birth_date = models.DateField('Fecha de nacimiento', blank=True, null=True)
    id_number = models.CharField(max_length=14)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.name

