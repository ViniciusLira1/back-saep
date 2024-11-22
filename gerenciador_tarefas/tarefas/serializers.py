from rest_framework import serializers
from .models import Usuario, Tarefa

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome_usuario', 'email']

class TarefaSerializer(serializers.ModelSerializer):
    nome_usuario = serializers.CharField(source='usuario.nome_usuario', read_only=True)
    
    class Meta:
        model = Tarefa
        fields = '__all__'

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'
