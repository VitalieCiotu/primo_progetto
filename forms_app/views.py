from django.shortcuts import render
from .forms import FormContatto
from django.http import HttpResponse
from .models import Contatto
from django.shortcuts import get_object_or_404 ,redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

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

            print("Salvo il contatto nel database")
            nuovo_contatto = form.save()
            print("new_post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)

            # Ringrazia l'utente per averci contattato -> volendo possiamo effettuare un redirect a una pagina specifica
            return HttpResponse("<h3>Grazie per averci contattato!</h3>")

    # Se la richiesta HTTP usa il metodo GET o qualsiasi altro metodo, allora creo il form di default vuoto
    else:
        form = FormContatto()

    # Arriviamo a questo punto se si tratta della prima volta che la pagina viene richiesta(con metodo GET),
    # se il form non è valido e ha errori
    context = {"form": form}
    return render(request, "contatto.html", context)


def lista_contatti(request):
    # Retrieve all the contacts from the Contatto model (not the FormContatto form)
    contatti = Contatto.objects.all()

    # Prepare the context to pass to the template
    context = {
        'contatti': contatti
    }

    # Render the list of contacts to a template with the context
    return render(request, 'lista_contatti.html', context)


@login_required(login_url="/accounts/login")
def modifica_contatto(request, pk):
    contatto = get_object_or_404(Contatto, id=pk)
    
    if request.method == "GET":
        fomr = FormContatto(instance=contatto)
    if request.method == "POST":
        form = FormContatto(request.POST, instance=contatto)
        if form.is_valid():
            form.save()
            return redirect('forms_app:lsita_contatti')
        
    context = {'form': form, 'contatto': contatto}
    return render(request, 'modifica_contatto.html', context)


@staff_member_required(login_url="/accounts/login")
def elimina_contatto(request,pk):
    contatto = get_object_or_404(Contatto, id=pk)
    if request.method == "POST":
        contatto.delete()
        return redirect('forms_app:lista_contatti')
    context = {'contatto': contatto}
    return render(request, 'elimina_contatto.html', context)
