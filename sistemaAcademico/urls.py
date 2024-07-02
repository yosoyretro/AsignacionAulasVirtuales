"""
URL configuration for sistemaAcademico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from administrativa.views import dashboard,usuarios,newUsuario,perfiles,aulaVirtual,eliminarUsuario,newPeril,eliminarPeril,cursos,newCurso,deleteCurso,paralelo,newParalelo,deleteParalelo,materia,newMateria,deleteMateria
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',dashboard,name="dashboard"),
    #USUARIO
    path('Matenimientos/usuarios/',usuarios,name="mantenimientosUsuarios"),
    path('NewUsuario/',newUsuario,name="newUsuario"),
    path('eliminarUsuario/<int:usuario_id>',eliminarUsuario,name="eliminar_usuario"),
    #PERFIL
    path('Matenimientos/perfiles/',perfiles,name="mantenimientosPerfiles"),
    path('NewPerfil/',newPeril,name="nuevo_perfil"),
    path('eliminarPerfil/<int:perfil_id>',eliminarPeril,name="eliminarPerfil"),
    #AULA VIRTUAL
    path('Matenimientos/AulaVirtual/',aulaVirtual,name="mantenimientosAulaVirtual"),
    #CURSO
    path('Matenimientos/Cursos/',cursos,name="mantenimientoCursos"),
    path('newCurso/',newCurso,name="nuevoCurso"),
    path('deleteCurso/<int:curso_id>',deleteCurso,name="deleteCurso"),
    #PARALELO
    path('Matenimientos/Paralelo/',paralelo,name="mantenimientoParalelos"),
    path('Matenimientos/NewParalelo/',newParalelo,name="NewParalelo"),
    path('eliminarParalelo/<int:paralelo_id>',deleteParalelo,name="deleteParalelo"),
    #MATERIAS
    path('Matenimientos/Materias/',materia,name="mantenimientoParalelos"),
    path('newMaterias/',newMateria,name="nuevaMateria"),
    path('eliminarMateria/<int:materia_id>',deleteMateria,name="deleteMateria"),
]
