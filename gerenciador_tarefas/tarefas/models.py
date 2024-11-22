from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome_usuario = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome_usuario

class Tarefa(models.Model):
    OPCOES_STATUS = [
        ('a_fazer', 'A Fazer'),
        ('fazendo', 'Fazendo'),
        ('pronto', 'Pronto'),
    ]

    OPCOES_PRIORIDADE = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, related_name='tarefas', on_delete=models.CASCADE)
    descricao = models.TextField()
    setor = models.CharField(max_length=100, default="Sem setor")
    prioridade = models.CharField(max_length=10, choices=OPCOES_PRIORIDADE)
    data_cadastro = models.DateTimeField(default=timezone.localtime)
    status = models.CharField(max_length=10, choices=OPCOES_STATUS, default='a_fazer')

    def __str__(self):
        return f"{self.descricao} - {self.usuario.nome_usuario}"
