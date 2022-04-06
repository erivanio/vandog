from django.contrib import admin
from rangefilter.filters import DateTimeRangeFilter

from .models import Plano, Aula


class AulaInline(admin.TabularInline):
    model = Aula
    extra = 0


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = (
        'pet',
        'plano',
        'avaliacao',
        'entrada',
        'saida',
    )
    list_filter = (
        ('entrada', DateTimeRangeFilter),
        ('saida', DateTimeRangeFilter),
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
            'fields': ('avaliacao', 'plano', 'periodo','entrada', 'saida')
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
        'qtd_semana',
        'periodo',
        'inicio',
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
