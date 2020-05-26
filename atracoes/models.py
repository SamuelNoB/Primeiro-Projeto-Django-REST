from django.db import models
from core.models import PontoTuristico

# Create your models here.


class Atracao(models.Model):
    name = models.CharField('Nome', max_length=150)
    description = models.TextField('Descrição', blank=True)
    opening_hours = models.TextField('Horario de funcionamento', blank=True)
    min_age = models.IntegerField('Idade mínima', default=0)
    photo = models.ImageField(upload_to='atracoes', null=True, blank=True)

    point = models.ForeignKey(PontoTuristico,
                              on_delete=models.CASCADE,
                              verbose_name='ponto_turistico',
                              related_name='attractions')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Atração'
        verbose_name_plural = 'Atrações'