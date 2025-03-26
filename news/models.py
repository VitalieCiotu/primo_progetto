from django.db import models

class Giornalista(models.Model):
    nome = models.CharField(max_length=20)  # Campo di testo con massimo 20 caratteri
    cognome = models.CharField(max_length=20)  # Cognome del giornalista
    anno_di_nascita = models.DateField(null=True, blank=True)  # Data di nascita (può essere vuoto)

    def __str__(self):
        return self.nome + " " + self.cognome  # Restituisce il nome completo nel pannello admin
    
    class Meta:
        verbose_name = "Giornalista"  # Nome singolare nel pannello admin
        verbose_name_plural = "Giornalisti"  # Nome plurale nel pannello admin

        

class Articolo(models.Model):
    """Il modello generico di un articolo di news"""
    titolo = models.CharField(max_length=100)  # Titolo dell'articolo (max 100 caratteri)
    contenuto = models.TextField()  # Testo dell'articolo (può essere lungo)
    giornalista = models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articolo")  
    visualizzazioni = models.IntegerField(default=0)  # Numero di visualizzazioni (default: 0)
    data = models.DateField(null=True, blank=True)  # Data di pubblicazione (facoltativa)

    def __str__(self):
        return self.titolo  # Mostra il titolo nell'admin
    
    class Meta:
        verbose_name = "Articolo"  
        verbose_name_plural = "Articoli" 

#python manage.py makemigrations
#python manage.py migrate

#python manage.py shell

#from news.models import Giornalista, Articolo  

# Creare un giornalista
#giornalista1 = Giornalista.objects.create(nome="Mario", cognome="Rossi", anno_di_nascita="1980-05-20")

# Creare un articolo associato al giornalista
#articolo1 = Articolo.objects.create(titolo="Notizia Importante", contenuto="Testo della notizia...", giornalista=giornalista1)

# Visualizzare tutti i giornalisti
#Giornalista.objects.all()

# Visualizzare tutti gli articoli scritti da un giornalista specifico
#Articolo.objects.filter(giornalista=giornalista1)

# Cancellare tutti gli articoli di un giornalista
#Articolo.objects.filter(giornalista=giornalista1).delete()

