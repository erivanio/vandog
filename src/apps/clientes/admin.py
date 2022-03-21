from django.contrib import admin

from .models import Cliente, Telefone, Pet


class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1


class PetInline(admin.StackedInline):
    model = Pet
    extra = 0


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'bairro', 'numero')
    inlines = [TelefoneInline, PetInline]
    search_fields = ['nome', 'cpf']

    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('nome', 'cpf', 'arquivos')
        }),
        ('Endereço', {
            'fields': ('endereco', 'numero', 'bairro')
        }),
    )


@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('numero', 'whatsapp', 'cliente')
    list_filter = ('whatsapp', 'cliente')
    search_fields = ['cliente__nome', 'cliente__cpf']
    raw_id_fields = ('cliente',)


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('dono', 'nome', 'raca', 'porte', 'data_nascimento')
    list_filter = ('dono', 'porte')
    raw_id_fields = ('dono',)
    search_fields = ['dono__nome', 'dono__cpf', 'nome']

    fieldsets = (
        (None, {
            'fields': ('nome', 'dono')
        }),
        ('Informações', {
            'fields': ('raca', 'porte', 'peso', 'data_nascimento')
        }),
        ('Observações', {
            'fields': ('alergias', 'observacoes')
        }),
    )
