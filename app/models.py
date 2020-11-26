from django.db import models

# Create your models here.
class Alvo(models.Model):
    nome = models.CharField(max_length=60)
    latitude = models.FloatField()
    longitude = models.FloatField()
    dt_expiracao = models.DateField()


    def __str__(self):
        return self.nome
