from django.shortcuts import render
import requests

def todos_view(request):
    try:
        response = request.get('https://jsonplaceholder.typicode.com/todos/')
        if response.status_code == 200:
            lista_todos = response.json()
            mesaggio_errore = None
        else:
            lista_todos = []
            mesaggio_errore = "Errore nel recupero dei dati. Codice di stato: " + str(response.status_code)
    except Exception as e:
        lista_todos = []
        mesaggio_errore = "Erroe nella conessione all'API: " + str(e)

    
    return render (request, 'todos.html', {
        'todos': lista_todos,
        'errore': mesaggio_errore
    })