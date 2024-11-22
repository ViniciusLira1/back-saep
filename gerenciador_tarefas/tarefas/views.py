from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario, Tarefa
from .serializers import UsuarioSerializer, TarefaSerializer
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import permissions

@api_view(['GET', 'POST'])
def usuario_view(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def tarefa_view(request):
    if request.method == 'GET':
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TarefaRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class TarefaDeleteAPIView(DestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


