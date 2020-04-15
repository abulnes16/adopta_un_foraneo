from django.db import models
from apps.users.models import Profile


class ApartmentType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Tipo de propiedad', max_length=100)

    class Meta:
        verbose_name = 'Tipo de Propiedad'
        verbose_name_plural = 'Tipos de Propiedad'

    def __str__(self):
        return self.name


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Usuario')
    content = models.TextField('Comentario')

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return self.user


class Apartment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descripcion de la propiedad')
    direction = models.CharField('Direccion', max_length=1000)
    requirements = models.TextField('Requisitos de alquiler')
    city = models.CharField('Ciudad', max_length=200)
    rent_price = models.FloatField('Precio de renta')
    type = models.ForeignKey(ApartmentType, on_delete=models.CASCADE, verbose_name='Tipo de propiedad')
    property_state = models.BooleanField('Rentado / No Rentado')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Dueño')
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, verbose_name='Comentarios')
    publication_date = models.DateField('Fecha de publicación', auto_now=True)

    class Meta:
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'

    def __str__(self):
        return self.title

