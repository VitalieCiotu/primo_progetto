from django.shortcuts import render
from .forms import FormContatto
from django.http import HttpResponse

def contatti(request):
    # Se la richiesta è di tipo POST, allora possiamo processare i dati
    if request.method == "POST":

        # Creiamo l'istanza del form e lo popoliamo con i dati della POST request (processo di "binding")
        form = FormContatto(request.POST)

        # is_valid() controlla se il form inserito è valido:
        if form.is_valid():
            # A questo punto possiamo usare i dati validi!
            # Tenere a mente che cleaned_data["nome_dato"] ci permette di accedere ai dati validati e convertiti in tipi standard di Python
            print("Il form è valido!")
            print("NOME:", form.cleaned_data["contenuto"])
            print("COGNOME:", form.cleaned_data["cognome"])
            print("EMAIL:", form.cleaned_data["email"])
            print("CONTENUTO:", form.cleaned_data["contenuto"])
            
            # Ringrazia l'utente per averci contattato -> volendo possiamo effettuare un redirect a una pagina specifica
            return HttpResponse("<h3>Grazie per averci contattato!</h3>")

    # Se la richiesta HTTP usa il metodo GET o qualsiasi altro metodo, allora creo il form di default vuoto
    else:
        form = FormContatto()

    # Arriviamo a questo punto se si tratta della prima volta che la pagina viene richiesta(con metodo GET),
    # se il form non è valido e ha errori
    context = {"form": form}
    return render(request, "contatto.html", context)
