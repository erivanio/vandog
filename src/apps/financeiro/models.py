from django.db import models
from django.utils import timezone


class TimestampedMixin(models.Model):
    created = models.DateTimeField('criado em', editable=False,
                                   blank=True, auto_now_add=True)
    modified = models.DateTimeField('modificado em', editable=False,
                                    blank=True, auto_now=True)

    class Meta:
        abstract = True


class Servico(TimestampedMixin):
    TIPO_SERVICO_CHOICES = [
        ('banho', 'Banho'),
        ('tosa', 'Tosa'),
        ('banho+tosa', 'Banho e tosa'),
        ('outros', 'Outros'),
    ]
    PAGAMENTO_CHOICES = [
        ('aguardando', 'Aguardando'),
        ('dinheiro', 'Dinheiro'),
        ('credito', 'Cartão de Crédito'),
        ('debito', 'Cartão de Débito'),
        ('transferencia', 'Transferência'),
        ('outros', 'Outros'),
    ]
    tipo_servico = models.CharField(
        'tipo de serviço',
        max_length=50,
        choices=TIPO_SERVICO_CHOICES,
        default='p')
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    pagamento = models.CharField(
        'tipo de pagamento',
        max_length=50,
        choices=PAGAMENTO_CHOICES,
        default='aguardando')
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.PROTECT)
    pets = models.ManyToManyField('clientes.Pet', null=True, blank=True)
    observacao = models.TextField('observação', null=True, blank=True)
    data_servico = models.DateTimeField(
        'data do serviço', default=timezone.now())

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.cliente.nome
