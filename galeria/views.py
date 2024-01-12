from django.shortcuts import get_object_or_404, render
from galeria.models import Fotografia

fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

# foto_para_adicionar = Fotografia(
# nome="Galáxia NGC 1079", legenda="nasa.org / NASA / Hubble", foto="ngc1079.jpg"
# )

# foto_para_adicionar.save()


def index(request):
    return render(request, "galeria/index.html", {"cards": fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, "galeria/imagem.html", {"fotografia": fotografia})


def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET["buscar"]
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})
