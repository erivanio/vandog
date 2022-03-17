from django.contrib import admin
from rangefilter.filters import DateTimeRangeFilter

from .models import Receita, Estoque, Funcionario, Despesa, Categoria


@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'item',
        'quantidade',
        'valor_sugerido',
    )
    readonly_fields = ('created', 'modified')
    search_fields = ['item',]

    fieldsets = (
        (None, {
            'fields': ('item', 'quantidade', 'valor_sugerido')
        }),
        ('Controle', {
            'fields': ('created', 'modified')
        }),
    )


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cliente',
        'pet_list',
        'pagamento',
        'valor',
        'data_servico',

    )
    raw_id_fields = ('cliente', 'pets')
    readonly_fields = ('created', 'modified')
    list_filter = (
        ('data_servico', DateTimeRangeFilter),
        'plano',
        'servico',
        'item_estoque',
    )
    search_fields = ['cliente__nome']

    fieldsets = (
        ('Cliente', {
            'fields': ('cliente', 'pets')
        }),
        ('Pagamento', {
            'fields': ('pagamento', 'valor')
        }),
        ('Tipo da receita', {
            'fields': ('plano', 'servico', 'item_estoque', 'qtd_item')
        }),
        (None, {
            'fields': ('observacao', 'data_servico')
        }),
        ('Controle', {
            'fields': ('created', 'modified')
        }),
    )

    def pet_list(self, obj):
        return u", ".join(o.nome for o in obj.pets.all())

    pet_list.short_description = 'Pets'


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'telefone',
        'email',
        'cargo',
    )
    search_fields = ['nome',]
    readonly_fields = ('created', 'modified')

    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('nome', 'cpf', 'arquivos')
        }),
        ('Endereço', {
            'fields': ('endereco', 'bairro')
        }),
        ('Informações para contato', {
            'fields': ('telefone', 'email')
        }),
        (None, {
            'fields': ('cargo',)
        }),
        ('Controle', {
            'fields': ('created', 'modified')
        }),
    )



@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
    )
    readonly_fields = ('created', 'modified')
    search_fields = ['nome',]

    fieldsets = (
        (None, {
            'fields': ('nome',)
        }),
        ('Controle', {
            'fields': ('created', 'modified')
        }),
    )


@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'categoria_list',
        'data_despesa',
        'valor',
    )
    list_filter = (
        ('data_despesa', DateTimeRangeFilter),
        'pagamento',
        'categorias',
    )
    search_fields = ['titulo', 'funcionario__nome', 'categorias__name']
    readonly_fields = ('created', 'modified')

    fieldsets = (
        (None, {
            'fields': ('titulo',)
        }),
        ('Informações', {
            'fields': ('observacao', 'funcionario', 'categorias', 'data_despesa')
        }),
        ('Pagamento', {
            'fields': ('pagamento', 'parcelas', 'valor')
        }),
        ('Controle', {
            'fields': ('created', 'modified')
        }),
    )

    def categoria_list(self, obj):
        return u", ".join(o.nome for o in obj.categorias.all())

    categoria_list.short_description = 'Categorias'