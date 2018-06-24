from django.db import models

class Quemado(models.Model):
    numero = models.CharField(max_length=24, null=True, blank=True)
    nombre = models.CharField(max_length=240, null=True, blank=True)

    def __unicode__(self):
        return '{} - {}'.format(self.numero, self.nombre)


class Denuncia(models.Model):
    numero = models.CharField(max_length=24, null=True, blank=True)
    latitud = models.FloatField(null=True, blank=True)
    longitud= models.FloatField(null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)

    def __unicode__(self):
        return self.numero


class Posicion(models.Model):
    numero = models.CharField(max_length=24, null=True, blank=True)
    latitud = models.FloatField(null=True, blank=True)
    longitud= models.FloatField(null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.numero


class Mensajes(models.Model):
    numero = models.CharField(max_length=24, null=True, blank=True)
    mensajes = models.CharField(max_length=10000, null=True, blank=True)

    def __unicode__(self):
        return self.numero


class Contactos(models.Model):
    numero = models.CharField(max_length=24, null=True, blank=True)
    contactos = models.CharField(max_length=10000, null=True, blank=True)

    def __unicode__(self):
        return self.numero