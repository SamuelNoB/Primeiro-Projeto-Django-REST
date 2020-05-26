from django.contrib.auth.models import User
from django.db import models
from core.models import PontoTuristico

# Create your models here.


class Avaliacao(models.Model):

    comment = models.TextField('Comentário', blank=True)
    rate = models.DecimalField('Nota', max_digits=3, decimal_places=2)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Usuário',
                             related_name='avaliacoes')

    point = models.ForeignKey(PontoTuristico,
                              on_delete=models.CASCADE,
                              verbose_name='Ponto turístico',
                              related_name='avaliacoes'
                              )


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'