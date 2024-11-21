from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    STATUS_CHOICES = [
        ('a_fazer', 'A Fazer'),
        ('fazendo', 'Fazendo'),
        ('pronto', 'Pronto'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tarefas')
    descricao = models.TextField()
    setor = models.CharField(max_length=100)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='a_fazer')
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.descricao
