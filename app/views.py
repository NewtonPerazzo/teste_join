import folium
from django.shortcuts import render, redirect, get_object_or_404
from app.forms import AlvoForm
from app.models import Alvo


def home(request):
    alvos = Alvo.objects.all()
    mapa = folium.Map(width=800, height=500, location=[14.2350, 51.9253], zoom_start=2)
    for alvo in alvos:
        folium.Marker(location=[alvo.latitude, alvo.longitude],
                      popup=alvo.nome +
                            '<a href="list/"><button class="botao">Ver</button></a>' +
                            '<a href="add_alvo"><button class="botao">Adicionar Alvo</button></a>').add_to(mapa)
    mapa.save('app/templates/mapa.html')
    return render(request, 'mapa.html', {'alvos': alvos})


def delete(request, id):
    alvo = get_object_or_404(Alvo, pk=id)
    alvo.delete()
    return redirect('/')


def list(request):
    lista = Alvo.objects.all().order_by('dt_expiracao')
    return render(request, 'list.html', {'lista': lista})


def edit_alvo(request, id):
    alvo = get_object_or_404(Alvo, pk=id)
    form = AlvoForm(instance=alvo)
    if request.method == 'POST':
        form = AlvoForm(request.POST, instance=alvo)
        if form.is_valid():
            alvo.save()
            return redirect('/')
        else:
            return render(request, 'edit_alvo.html', {'form': form, 'alvo': alvo})
    else:
        return render(request, 'edit_alvo.html', {'form': form, 'alvo': alvo})


def add_alvo(request):
    if request.method == 'POST':
        form = AlvoForm(request.POST)
        if form.is_valid():
            alvo = form.save(commit=False)
            alvo.save()
            return redirect('/')
    else:
       form = AlvoForm
    return render(request, 'add_alvo.html', {'form': form})
