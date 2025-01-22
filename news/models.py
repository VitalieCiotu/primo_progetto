from django.db import models

class Giornalista(models.Model):
    nome = models.CharField(max_length=20)  # Parametro obbligatorio
    cognome = models.CharField(max_length=20)
    anno_di_nascita = models.DateField(null=True, blank=True)  # Nuovo campo aggiunto

    def __str__(self):
        return self.nome + " " + self.cognome
    
    class Meta:
        verbose_name = "Giornalista"
        verbose_name_plural = "Giornalisti"
        
    

class Articolo(models.Model):
    """Il modello generico di un articolo di news"""
    titolo = models.CharField(max_length=100)  # alcuni campi necessitano di parametri obbligatori
    contenuto = models.TextField()
    giornalista = models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articolo")
    visualizzazioni = models.IntegerField(default=0)  # Aggiungi questo campo
    data = models.DateField(null=True, blank=True)  # Aggiungi un campo "data" per la data dell'articolo

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"


