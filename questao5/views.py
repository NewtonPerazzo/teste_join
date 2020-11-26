from django.shortcuts import render

# Create your views here.
from questao5.models import Cliente, Produto, Pedido


def home(request):
    clientes = Cliente.objects.all()
    pedido = Pedido.objects.all()
    return render(request, 'questao5.html', {'clientes': clientes, 'pedido': pedido})