from django.db import models

class Contatto(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    contenuto = models.TextField()

    def __str__(self):
        return f"{self.nome} {self.cognome}"
    

