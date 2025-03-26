from django.contrib import admin
from django.urls import path#,include
from .views import contatti

app_name = "forms_app"

urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
]
