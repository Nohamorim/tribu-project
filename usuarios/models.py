from datetime import date
from django.db import models

class Cliente (models.Model):
    class Sexo(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'

    nome = models.CharField("Nome completo", max_length=100)
    data_nascimento = models.DateField("Data de nascimento", blank=True, null=True)
    sexo = models.CharField("Sexo", max_length=1, choices=Sexo.choices)
    email = models.EmailField("E-mail", blank=True, null=True)

    def __str__(self):
        return self.nome

class Publicacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='publicacoes')
    data_publicacao = models.DateField("Data da publicação", default=date.today)
    conteudo = models.TextField("Conteúdo da publicação")

    def __str__(self):
        return f"Publicação de {self.cliente.nome} em {self.data_publicacao}"
    class Meta:
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"
        ordering = ['-data_publicacao']
