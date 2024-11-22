from django.contrib import admin
from django.urls import path

from tarefas.views import usuario_view,TarefaRetrieveUpdateAPIView,TarefaDeleteAPIView,tarefa_view


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin do Django

    # Endpoints para usuários
    path('api/usuarios/', usuario_view, name='listar_usuarios'),  # Listar usuários (GET) e cadastrar (POST)
    path('api/usuarios/cadastrar/', usuario_view, name='cadastrar_usuario'),  # Cadastrar novo usuário
    path('api/tarefas/alterar/<int:pk>/', TarefaRetrieveUpdateAPIView.as_view(), name='alterar_usuario'),  
    path('api/tarefas/deletar/<int:pk>/', TarefaDeleteAPIView.as_view(), name='deletar_usuario'),  
    path('api/tarefas/cadastrar/', tarefa_view, name='cadastrar_tarefa'),
    path('api/tarefas/',tarefa_view,name='listar_tarefas'),
    path('api/tarefas/alterar_status/<int:pk>/', TarefaRetrieveUpdateAPIView.as_view(), name='alterar_status_tarefa'),  # Alterar status da tarefa
]
