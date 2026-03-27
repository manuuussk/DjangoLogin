from django.db import models

class Tarefas(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=False, blank=False)
    data = models.DateField()
    status = models.BooleanField()

    def _str_(self):
        return self.titulo