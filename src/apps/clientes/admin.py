from django.contrib import admin

from .models import Cliente, Telefone, Pet


class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1


class PetInline(admin.StackedInline):
    model = Pet
    extra = 1


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'bairro', 'numero')
    inlines = [TelefoneInline, PetInline]

    fieldsets = (
        (None, {
            'fields': ('nome',)
        }),
        ('Endereço', {
            'fields': ('endereco', 'numero', 'bairro')
        }),
    )


@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'whatsapp', 'cliente')
    list_filter = ('whatsapp', 'cliente')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'dono', 'nome', 'raca', 'porte', 'data_nascimento')
    list_filter = ('dono', 'porte')
