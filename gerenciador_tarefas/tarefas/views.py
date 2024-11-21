from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Tarefa
from .serializers import UsuarioSerializer, TarefaSerializer
from rest_framework.decorators import api_view

# Criar um novo usuário
class CadastrarUsuario(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Alterar um usuário
class AlterarUsuario(APIView):
    def put(self, request, pk):
        try:
            usuario = Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuário não encontrado!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UsuarioSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Deletar um usuário
class DeletarUsuario(APIView):
    def delete(self, request, pk):
        try:
            usuario = Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuário não encontrado!"}, status=status.HTTP_404_NOT_FOUND)
        
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Criar uma nova tarefa para um usuário
class CadastrarTarefa(APIView):
    def post(self, request, usuario_id):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuário não encontrado!"}, status=status.HTTP_404_NOT_FOUND)
        
        # Adicionando o ID do usuário automaticamente
        request.data['usuario'] = usuario.id
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Alterar o status de uma tarefa
class AlterarStatusTarefa(APIView):
    def put(self, request, pk):
        try:
            tarefa = Tarefa.objects.get(pk=pk)
        except Tarefa.DoesNotExist:
            return Response({"error": "Tarefa não encontrada!"}, status=status.HTTP_404_NOT_FOUND)
        
        # Atualizando apenas o status da tarefa
        tarefa.status = request.data.get('status', tarefa.status)
        tarefa.save()
        return Response(TarefaSerializer(tarefa).data)
