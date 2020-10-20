from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField('endereço', max_length=200)
    bairro = models.CharField(max_length=200)
    numero = models.CharField('número', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    numero = models.CharField('número', max_length=50)
    whatsapp = models.BooleanField(default=True)
    cliente = models.ForeignKey(
        'Cliente', on_delete=models.CASCADE, related_name='telefones')

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    def __str__(self):
        return self.numero


class Pet(models.Model):
    PORTE_CHOICES = [
        ('p', 'Pequeno'),
        ('m', 'Médio'),
        ('g', 'Grande'),
    ]
    dono = models.ForeignKey(
        'Cliente', on_delete=models.CASCADE, related_name='pets')
    nome = models.CharField(max_length=200)
    raca = models.CharField('raça', max_length=200, null=True, blank=True)
    porte = models.CharField(
        max_length=1, choices=PORTE_CHOICES, default='p')
    data_nascimento = models.DateField(
        'data de nascimento', null=True, blank=True)

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

    def __str__(self):
        return self.nome
