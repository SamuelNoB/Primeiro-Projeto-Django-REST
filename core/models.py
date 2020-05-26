from django.db import models
from enderecos.models import Endereco

# Create your models here.


class PontoTuristico(models.Model):
    name = models.CharField('Nome', max_length=150)
    description = models.TextField('Descrição', blank=True)
    is_approved = models.BooleanField('Status', default=False)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    address = models.OneToOneField(Endereco,
                                   on_delete=models.CASCADE,
                                   verbose_name='Endereço',
                                   related_name='pontos_turisticos',
                                   )

    photo = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    @property
    def complete_description2(self):
        return '%s - %s ' % (self.name, self.description)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ponto Turístico"
        verbose_name_plural = 'Pontos Turísticos'
