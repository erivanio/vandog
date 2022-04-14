from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from .models import Plano, Aula


class AulaInline(admin.TabularInline):
    model = Aula
    extra = 0
    exclude = ['avaliacao',]
    raw_id_fields = ('pet',)


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = (
        'pet',
        'plano',
        'avaliacao',
        'data_aula',
    )
    list_filter = (
        ('data_aula', DateRangeFilter),
        'periodo',
        'avaliacao',
    )
    readonly_fields = ('created', 'modified')
    search_fields = ['pet__nome', 'pet__dono__nome', 'pet__dono__cpf']
    raw_id_fields = ('pet', 'plano')

    fieldsets = (
        ('Aluno', {
            'fields': ('pet',)
        }),
        ('Período', {
            'fields': ('avaliacao', 'plano', 'periodo', 'data_aula')
        }),
        ('Controle', {
            'fields': ('created', 'modified')
        }),
    )


@admin.register(Plano)
class PlanoaAdmin(admin.ModelAdmin):
    list_display = (
        'pet',
        'periodo',
        'qtd_semana',
        'inicio',
    )
    list_filter = (
        ('inicio', DateRangeFilter),
        'qtd_semana',
        'periodo',
    )
    raw_id_fields = ('pet',)
    readonly_fields = ('created', 'modified')
    search_fields = ['pet__nome', 'pet__dono__nome', 'pet__dono__cpf']
    inlines = [AulaInline,]

    fieldsets = (
        ('Aluno', {
            'fields': ('pet',)
        }),
        ('Período', {
            'fields': ('qtd_semana', 'periodo', 'inicio')
        }),
        ('Controle', {
            'fields': ('created', 'modified')
        }),
    )
