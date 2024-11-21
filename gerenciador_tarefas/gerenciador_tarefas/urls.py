from django.contrib import admin
from django.urls import path
from tarefas.views import CadastrarUsuario, AlterarUsuario, DeletarUsuario, CadastrarTarefa, AlterarStatusTarefa

urlpatterns = [
    path('admin/', admin.site.urls),          # Admin do Django

    # Endpoints para usuários
    path('api/usuarios/cadastrar/', CadastrarUsuario.as_view(), name='cadastrar_usuario'),
    path('api/usuarios/alterar/<int:pk>/', AlterarUsuario.as_view(), name='alterar_usuario'),
    path('api/usuarios/deletar/<int:pk>/', DeletarUsuario.as_view(), name='deletar_usuario'),

    # Endpoints para tarefas
    path('api/tarefas/cadastrar/<int:usuario_id>/', CadastrarTarefa.as_view(), name='cadastrar_tarefa'),
    path('api/tarefas/alterar_status/<int:pk>/', AlterarStatusTarefa.as_view(), name='alterar_status_tarefa'),
]
