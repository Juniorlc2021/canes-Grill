from django.db import models

# Create your models here.
class pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome