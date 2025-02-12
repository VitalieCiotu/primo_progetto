from django.db import models

class Corso(models.Model):
    titolo = models.CharField(max_length=30)
    descrizione = models.TextField(max_length=100)
    data_inizio = models.DateField(null=True, blank=True)
    data_fine = models.DateField(null=True, blank=True)
    posti_disponibili = models.IntegerField(default=0)

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name = "Corso"  
        verbose_name_plural = "Corsi" 