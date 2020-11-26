from django.shortcuts import render
from django.utils.timezone import now

from questao1.models import Pessoas, Cargos


# Create your views here.


def home(request):
    a = Pessoas.objects.all().order_by('admissao')
    cargos = Cargos.objects.all()
    lista_de_ids = []
    lista_pessoa_id = []
    lista_pessoa = []
    for cargo in cargos:
        lista_de_ids.append(cargo.id)
    for i in lista_de_ids:
        pessoa = Pessoas.objects.filter(cargo=i)
        lista_pessoa.append(pessoa.count())

    for pessoa in a:
        lista_admissoes = [pessoa.admissao]
        mais_antigo = pessoa.buscarMenor(lista_admissoes)
        dados_mais_antigo = Pessoas.objects.get(admissao=mais_antigo)
        return render(request, 'questao1.html', {'a': a, 'mais_antigo': dados_mais_antigo, 'cargos': cargos, 'qtd': lista_pessoa})
