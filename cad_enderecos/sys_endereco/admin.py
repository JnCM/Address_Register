from django.contrib import admin
from sys_endereco.models import Endereco
# Register your models here.
#admin.site.register(Endereco)
@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cep', 'logradouro', 'bairro', 'numero', 'cidade', 'uf', 'complemento', 'descricao')
