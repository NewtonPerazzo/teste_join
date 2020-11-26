from django.db import models

# Create your models here.
class Cargos(models.Model):
    nome_cargo = models.CharField(max_length=300)

    def __str__(self):
        return self.nome_cargo

class Pessoas(models.Model):
    nome = models.CharField(max_length=200)
    admissao = models.DateField()
    cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)


    def buscarMenor(self, lista):
        menor = lista[0]
        for i in lista:
            if i < menor:
                menor = i
        return menor

    def __str__(self):
        return self.nome