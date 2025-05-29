from datetime import date
from django.db import models


class Cliente(models.Model):
    class Sexo(models.TextChoices):
        MASCULINO = "M", "Masculino"
        FEMININO = "F", "Feminino"

    nome = models.CharField("Nome completo", max_length=100)
    data_nascimento = models.DateField("Data de nascimento", blank=True, null=True)
    sexo = models.CharField("Sexo", max_length=1, choices=Sexo.choices)
    email = models.EmailField("E-mail", blank=True, null=True)

    def __str__(self):
        return self.nome
