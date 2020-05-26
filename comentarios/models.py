from django.contrib.auth.models import User
from django.db import models
from core.models import PontoTuristico



# Create your models here.
class Comentario(models.Model):
    comment = models.TextField('Comentário', blank=True)
    approved = models.BooleanField('Status', default=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Usuário',
                             related_name='comentarios'
                             )
    point = models.ForeignKey(PontoTuristico,
                             on_delete=models.CASCADE,
                             verbose_name='Ponto Turístico',
                             related_name='comentarios'
                             )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'