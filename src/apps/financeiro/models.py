from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver


class TimestampedMixin(models.Model):
    created = models.DateTimeField('criado em', editable=False,
                                   blank=True, auto_now_add=True)
    modified = models.DateTimeField('modificado em', editable=False,
                                    blank=True, auto_now=True)

    class Meta:
        abstract = True


class Estoque(TimestampedMixin):
    item = models.CharField('item', max_length=150)
    quantidade = models.IntegerField('quantidade', default=0)
    valor_sugerido = models.DecimalField('valor sugerido', max_digits=5,
        decimal_places=2)

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Itens em Estoque'

    def __str__(self):
        return self.item

class Receita(TimestampedMixin):
    TIPO_SERVICO_CHOICES = [
        ('', 'Escolha um serviço'),
        ('avaliacao', 'Avaliação'),
        ('meioperiodo', 'Daycare meio periodo'),
        ('integral', 'Daycare periodo integral'),
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
    servico = models.CharField('tipo de serviço', max_length=50,
        choices=TIPO_SERVICO_CHOICES, null=True, blank=True)
    plano = models.ForeignKey('planos.Plano', on_delete=models.PROTECT,
        null=True, blank=True)
    aula = models.ForeignKey('planos.Aula', on_delete=models.PROTECT,
        null=True, blank=True)
    item_estoque = models.ForeignKey('Estoque', on_delete=models.PROTECT,
        null=True, blank=True)
    qtd_item = models.IntegerField('Quantidade de itens', default=0,
        help_text="Referente aos itens em estoque que foram vendidos")
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.PROTECT)
    pets = models.ManyToManyField('clientes.Pet')
    observacao = models.TextField('observação', null=True, blank=True)
    data_servico = models.DateTimeField(
        'data do serviço', default=timezone.now)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    pagamento = models.CharField('tipo de pagamento', max_length=50,
        choices=PAGAMENTO_CHOICES, default='aguardando')

    def clean(self):
        if self.item_estoque:
            if self.item_estoque.quantidade < self.qtd_item:
                raise ValidationError({'qtd_item': 'Estoque insuficiente!'})

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'

    def __str__(self):
        return self.cliente.nome


class Funcionario(TimestampedMixin):
    nome = models.CharField(max_length=250)
    cpf = models.CharField('CPF', max_length=14, default='000.000.000-00')
    endereco = models.CharField('endereço', max_length=250)
    bairro = models.CharField(max_length=200)
    telefone = models.CharField('telefone', max_length=50)
    email = models.CharField('email', max_length=200)
    cargo = models.CharField(max_length=250)
    arquivos = models.URLField('arquivos', null=True, blank=True,
        help_text='Endereço para pasta de arquivos')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Categoria(TimestampedMixin):
    nome = models.CharField('item', max_length=150)

    class Meta:
        verbose_name = 'Categoria da Despesa'
        verbose_name_plural = 'Categorias da Despesa'

    def __str__(self):
        return self.nome


class Despesa(TimestampedMixin):
    PAGAMENTO_CHOICES = [
        ('avista', 'À vista'),
        ('parcelado', 'Parcelado'),
    ]
    titulo = models.CharField('título', max_length=250)
    funcionario = models.ForeignKey('Funcionario', on_delete=models.PROTECT,
        null=True, blank=True)
    categorias = models.ManyToManyField('Categoria', blank=True)
    observacao = models.TextField('observação', null=True, blank=True)
    data_despesa = models.DateTimeField(
        'data do pagamento', default=timezone.now)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    pagamento = models.CharField('tipo de pagamento', max_length=50,
        choices=PAGAMENTO_CHOICES, default='aguardando')
    parcelas = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'

    def __str__(self):
        return self.titulo


@receiver(post_save, sender=Receita)
def debita_estoque(sender, instance, **kwargs):
    if instance.item_estoque:
        instance.item_estoque.quantidade -= instance.qtd_item
        instance.item_estoque.save()

post_save.connect(debita_estoque, sender=Receita)