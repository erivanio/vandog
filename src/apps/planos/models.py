from django.db import models
from apps.financeiro.models import TimestampedMixin
from datetime import date
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Plano(TimestampedMixin):
    QUANTIDADE_CHOICES = [
        ('', 'Escolha quantas vezes por semmana'),
        ('1', '1x por semana'),
        ('2', '2x por semana'),
        ('3', '3x por semana'),
        ('4', '4x por semana'),
        ('5', '5x por semana'),
    ]
    PERIODO_CHOICES = [
        ('', 'Escolha um periodo'),
        ('meio', 'meio período'),
        ('integral', 'período integral'),
    ]
    qtd_semana = models.CharField('Vezes por semana', max_length=50,
        choices=QUANTIDADE_CHOICES, null=True, blank=True)
    periodo = models.CharField('Período', max_length=50,
        choices=PERIODO_CHOICES, null=True, blank=True)
    pet = models.ForeignKey('clientes.Pet', on_delete=models.PROTECT)
    inicio = models.DateField('início', default=date.today)
    
    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'

    def __str__(self):
        return '%s(%s-%s)' % (self.pet.nome, self.qtd_semana, self.periodo)


class Aula(TimestampedMixin):
    PERIODO_CHOICES = [
        ('', 'Escolha um periodo'),
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('integral', 'Integral')
    ]
    pet = models.ForeignKey('clientes.Pet', on_delete=models.PROTECT)
    plano = models.ForeignKey('Plano', on_delete=models.PROTECT,
        null=True, blank=True)
    avaliacao = models.BooleanField('avaliação', default=False)
    periodo = models.CharField('período da aula', max_length=50,
        choices=PERIODO_CHOICES, null=True, blank=True)
    data_aula = models.DateField('data da aula', default=date.today)
    
    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'

    def __str__(self):
        return '%s(%s)' % (self.pet.nome, self.pet.dono.nome)


@receiver(pre_save, sender=Aula)
def seleciona_plano_pet(sender, instance, **kwargs):
    if instance.plano:
        instance.pet = instance.plano.pet

pre_save.connect(seleciona_plano_pet, sender=Aula)