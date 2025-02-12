from .views import elencoCorsiOrdinato, indexCorsi, corsiDataInizio, corsiPostiDisponibili, corsiDataTermina, postiCorso
from django.urls import path
from django.contrib import admin


app_name="corsi_formazione"


urlpatterns = [
    path('', indexCorsi, name='indexCorsi'),
    path('Corsi_Ordinati', elencoCorsiOrdinato, name='Corsi_Ordinati'),
    #path('corsoDetail', corsoDetail, name='corsoDetail'),
    path('corsiDataInizio', corsiDataInizio, name='corsiDataInizio'),
    path('corsiPostiDisponibili', corsiPostiDisponibili, name='corsiPostiDisponibili'),
    path('corsiDataTermina', corsiDataTermina, name='corsiDataTermina'),
    path('postiCorso', postiCorso, name='postiCorso'),

]