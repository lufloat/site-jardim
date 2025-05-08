from django.shortcuts import render, get_object_or_404

from galeria.models import jardins

def index(request):
    jardins_details = jardins.objects.order_by("data_jardins").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": jardins_details})

def imagem(request, foto_id):
    jardins_details = get_object_or_404(jardins, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"jardins": jardins_details})

def buscar(request):
    jardins_details = jardins_details.objects.order_by("data_jardins").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET["buscar"]
        if nome_a_buscar:
            jardins_details = jardins_details.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"jardins": jardins_details})
