from django.db import models
from datetime import datetime

class jardins(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)    
    publicada = models.BooleanField(default=False)
    data_jardins = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"jardins [nome={self.nome}]"