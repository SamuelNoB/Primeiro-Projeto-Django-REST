from django.contrib.gis.db import models


# Create your models here.


class Endereco(models.Model):
    """
    line1 = models.CharField('Linha1', max_length=150)
    line2 = models.CharField('Linha2', max_length=150)
    city = models.CharField('Cidade', max_length=150)
    state = models.CharField('Estado', max_length=150)
    country = models.CharField('País', max_length=150)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)
    """
    location = models.PointField(verbose_name='coordenadas', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.location)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'