from django.db import models


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Mensajes de Contacto'
        verbose_name_plural = 'Mensajes de contacto'

    def __str__(self):
        return self.name
