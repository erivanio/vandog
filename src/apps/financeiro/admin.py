from django.contrib import admin

from .models import Servico


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'tipo_servico',
        'valor',
        'pagamento',
        'cliente',
        'observacao',
        'data_servico',

    )
    readonly_fields = ('created', 'modified')
    list_filter = ('created', 'modified', 'data_servico')
    raw_id_fields = ('cliente', 'pets')

    fieldsets = (
        ('Agendamento', {
            'fields': ('cliente', 'pets', 'tipo_servico', 'data_servico')
        }),
        ('Pagamento', {
            'fields': ('pagamento', 'valor')
        }),
        (None, {
            'fields': ('observacao',)
        }),
        ('Controle', {
            'fields': ('created', 'modified')
        }),
    )
