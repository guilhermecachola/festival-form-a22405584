from django.shortcuts import get_object_or_404, redirect, render
from .models import Dia, Palco, Concerto               
from .forms import ConcertoForm, PalcoForm


def index_view(request):
    return render(request, 'festival/index.html')

def dias_view(request):
    dias = Dia.objects.all()

    context = {'dias': dias}

    return render(request, 'festival/dias.html', context)

def apagar_concerto_view(request, concerto_id):
    concerto = get_object_or_404(Concerto, id=concerto_id)
    
    if request.method == 'POST':
        concerto.delete()
        return redirect('dias')  
    
   
    return redirect('concerto', concerto_id=concerto.id)

def novo_concerto_view(request):
    if request.method == 'POST':
        form = ConcertoForm(request.POST)
        if form.is_valid():
            # Guarda o novo concerto na base de dados
            novo_concerto = form.save()
            # Redireciona para a página do concerto acabado de criar
            return redirect('concerto', concerto_id=novo_concerto.id)
    else:
        # Se for um acesso normal, mostra o formulário vazio
        form = ConcertoForm()

    return render(request, 'festival/novo_concerto.html', {'form': form})

def editar_palco_view(request, palco_id):
    palco = get_object_or_404(Palco, id=palco_id)
    
    if request.method == 'POST':
        # request.FILES é necessário por causa da imagem do palco
        form = PalcoForm(request.POST, request.FILES, instance=palco)
        if form.is_valid():
            form.save()
            return redirect('palcos')
    else:
        form = PalcoForm(instance=palco)
        
    return render(request, 'festival/editar_palco.html', {'form': form, 'palco': palco})
    
def palcos_view(request):
    palcos = Palco.objects.all() 

    context = {'palcos': palcos}

    return render(request, 'festival/palcos.html', context)


def concerto_view(request, concerto_id):
    concerto = Concerto.objects.get(id=concerto_id)

    context = {'concerto': concerto}

    return render(request, 'festival/concerto.html', context)


def editar_concerto_view(request, concerto_id):
    concerto = get_object_or_404(Concerto, id=concerto_id)

    if request.method == 'POST':
        form = ConcertoForm(request.POST, instance=concerto)
        if form.is_valid():
            form.save()
            return redirect('concerto', concerto_id=concerto.id)
    else:
        form = ConcertoForm(instance=concerto)

    context = {
        'concerto': concerto,
        'form': form,
    }

    return render(request, 'festival/editar_concerto.html', context)
