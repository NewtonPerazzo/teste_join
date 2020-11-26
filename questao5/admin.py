from django.contrib import admin

# Register your models here.
from questao5.models import Cliente, Endereco, Produto, Pedido

admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Produto)
admin.site.register(Pedido)
