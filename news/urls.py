from .views import indexNews, home, ArticoloDetailView, listaArticoli, queryBase
from django.urls import path
from django.contrib import admin


app_name="news"

#urlpatterns = {
    #path('home', home, name='homeview'),
    #path('articoli/<int:pk>', articoloDetailView, name='articolo_detail'),
    #path('lista_articoli', listaArticoli, name='lista_articoli_giornalista'),
    #path('lista_articoli/<int:pk>', listaArticoli, name='lista_articoli_giornalista'),
    #path('queryBase', queryBase, name='queryBase'),
    #path('', index, name='indexNews'),
#}

urlpatterns = [
    path('', indexNews, name='indexNews'),
    path('home/', home, name='homeview'),
    path('articoli/<int:pk>/', ArticoloDetailView, name='ArticoloDetailView'),
    path('listaArticoli/<int:pk>/', listaArticoli, name='listaArticoli'),
    path('listaArticoli/', listaArticoli, name='listaArticoli'),
    path('query/', queryBase, name='query'),

    # Rimuovi o sostituisci la route per queryBase se non esiste
]