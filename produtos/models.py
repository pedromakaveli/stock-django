from django.db import models

# Create your models here.

class Marca (models.Model):
    nome = models.CharField(max_length=100)

    def __str__ (self):
        return self.nome


class Produto (models.Model):
    nome = models.CharField(max_length=150)
    tipo = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    
    def __str__ (self):
        return self.nome
    
class Tipo (models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome