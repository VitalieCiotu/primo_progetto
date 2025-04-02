from django.contrib import admin
from django.urls import path#,include
from .views import contatti, lista_contatti

app_name = "forms_app"

urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
    path('lista_contatti/', lista_contatti, name='lista_contatti'),

]
