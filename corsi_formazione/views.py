from django.shortcuts import get_object_or_404, render
from .models import Corso
import datetime 
from django.http import HttpResponse

def indexCorsi(request):
    return render(request, "indexCorsi.html")

def elencoCorsiOrdinato(request):
    Corsi = Corso.objects.order_by('data_inizio')
    context = {
        'Corsi': Corsi,
    }
    return render(request, 'view_a.html', context)

#def corsoDetail(request, pk):

    #context = {
    
    #}
    #return render(request, "view_b.html", context)

def corsiDataInizio(request):
    Corsi = Corso.objects.filter(data_inizio__gte=datetime.date(2025, 5, 1))
    context = {
        'Corsi':Corsi,
    }
    return render(request, 'view_c.html', context)

def corsiPostiDisponibili(request):
    Corsi = Corso.objects.filter(posti_disponibili__gte=20).distinct()
    context = {
        'Corsi':Corsi,
    }
    return render(request, 'view_d.html', context)

def corsiDataTermina(request):
    Corsi = Corso.objects.filter(data_fine__lt=datetime.date(2025, 4, 30))
    context = {
        'Corsi':Corsi,
    }
    return render(request, 'view_e.html', context)

def postiCorso(request):
    CorsiMD = Corso.objects.order_by('-posti_disponibili').first()
    CorsimD = Corso.objects.order_by('-posti_disponibili').last()

    context = {
        'CorsiMD':CorsiMD,
        'CorsimD':CorsimD,

    }
    return render(request, 'view_f.html', context)