from django.db import models
from apps.financeiro.models import TimestampedMixin
from django.utils import timezone


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
    MESES_CHOICES = [
        ('', 'Escolha um periodo'),
        ('janeiro', 'Janeiro'),
        ('fevereiro', 'fevereiro'),
        ('março', 'Março'),
        ('abril', 'Abril'),
        ('maio', 'Maio'),
        ('junho', 'Junho'),
        ('julho', 'Julho'),
        ('agosto', 'Agosto'),
        ('setembro', 'Setembro'),
        ('outubro', 'Outubro'),
        ('novembro', 'Novembro'),
        ('dezembro', 'Dezembro')
    ]
    qtd_semana = models.CharField('Vezes por semana', max_length=50,
        choices=QUANTIDADE_CHOICES, null=True, blank=True)
    periodo = models.CharField('Período', max_length=50,
        choices=PERIODO_CHOICES, null=True, blank=True)
    pet = models.ForeignKey('clientes.Pet', on_delete=models.PROTECT)
    mes_referencia = models.CharField('Mês referência', max_length=50,
        choices=MESES_CHOICES, null=True, blank=True)
    
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
    entrada = models.DateTimeField(
        'entrada', default=timezone.now)
    saida = models.DateTimeField(
        'saida', default=timezone.now)
    
    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'

    def __str__(self):
        return '%s(%s)' % (self.pet.nome, self.pet.dono.nome)
