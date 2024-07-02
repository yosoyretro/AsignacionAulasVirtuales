from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from administrativa.models import Perfil,Usuarios,Curso,Paralelo,Materia
from django.db.models import Q
# Create your views here.
#DASHBOARD

def dashboard(request):
    return render(request,"dashboard",{})

def definaMensajes(request_param):
    mensaje = None
    storage = messages.get_messages(request_param)
    
    for message in storage:
        if message.level == messages.SUCCESS or message.level == messages.ERROR or mensaje.level == mensaje.WARNING:
            mensaje = {
                "mensaje" : message,
                "tipo" : message.level_tag
            }
        else:
            mensaje = None
    return mensaje

#USUARIOS
def usuarios(request):
    storage = messages.get_messages(request)
    mensaje = None
    for message in storage:
        if message.level == messages.SUCCESS or message.level == messages.ERROR or mensaje.level == mensaje.WARNING:
            mensaje = {
                "mensaje" : message,
                "tipo" : message.level_tag
            }
        else:
            mensaje = None
    usuarios = Usuarios.objects.filter(estado="A",
                                       id_perfil__estado="A")
    
    return render(request,"Mantenimientos/usuarios",{
        'usuarios':usuarios,
        "mensaje":mensaje,
    })

def newUsuario(request):
    perfilesOnject = Perfil.objects.filter(estado="A")
    if(request.method == "POST"):
        data = request.POST
        perfil = perfilesOnject.get(id = data.get('perfil'))
        usuario = Usuarios.objects.create(
            cedula = data.get('cedula'),
            nombres = data.get('nombres'),
            apellidos = data.get('apellidos'),
            edad = data.get('edad'),
            genero = data.get('genero'),
            pais_natal = data.get('pais'),
            ciudad_natal = data.get('ciudad'),
            id_perfil = perfil,
            estado="A"
        )
        if(usuario):
            messages.success(request,"Usuario creado con exito")
            return redirect('mantenimientosUsuarios')
    return render(request,"Mantenimientos/newUsuario",{
        'perfiles':perfilesOnject
    })

def eliminarUsuario(request,usuario_id):
    obj_usuario = get_object_or_404(Usuarios,pk=usuario_id)
    if obj_usuario:
        obj_usuario.estado = "E"
        obj_usuario.save()
        messages.success(request,"Usuario Eliminado exitosamente")
        
    return redirect('mantenimientosUsuarios')

#PERFILES
def perfiles(request):
    perfiles = Perfil.objects.filter(estado="A")
    mensaje = definaMensajes(request)
    
    return render(request,"Mantenimientos/perfil",{
        "perfiles":perfiles,
        "mensaje":mensaje
    })

def eliminarPeril(request,perfil_id):
    try:
        perfil_obj = get_object_or_404(Perfil,pk=perfil_id)
        if perfil_obj:
            perfil_obj.estado = "E"
            perfil_obj.save()
            messages.success(request,"Perfil eliminado exitosamente")
    except:
        messages.error(request,"A ocurrido un error al eliminar el perfil")
    return redirect('mantenimientosPerfiles')

def newPeril(request):
    if request.method == "POST":
        data_perfil = request.POST
        
        perfil = Perfil.objects.create(
            descripcion= data_perfil.get('inputPerfil'),
            estado="A"
            )
        perfil = perfil.save()
        try:
            messages.success(request,"Perfil creado exitosamente")
        except:
            messages.error(request,"A ocurrido un error al crear el perfil")
    return redirect("mantenimientosPerfiles")

#CURSO
def cursos(request):
    mensaje = definaMensajes(request)
    cursos = Curso.objects.filter(estado="A")
    
    return render(request,'Mantenimientos/Curso',{
        "mensaje":mensaje,
        "cursos":cursos
    })

def newCurso(request):
    try:
        if(request.method == "POST"):
            data_curso = request.POST
            obj_curso = Curso.objects.create(curso = data_curso.get('inputCurso'),numero = data_curso.get('inputCursoNumber'),estado="A")
            obj_curso.save()
            messages.success(request,'Cursos creado con exito')
    except:
        messages.error(request,"A ocurrido un error al crear el curso")   
    return redirect("mantenimientoCursos")

def deleteCurso(request,curso_id):
    try:
        obj_curso = get_object_or_404(Curso,pk=curso_id)
        if(obj_curso):
            obj_curso.estado = "E"
            obj_curso.save()
            messages.success(request,'Curso eliminado exitosamente')
        else:
            messages.warning(request,f'El curso no existe con el id {id_curso}')
    except:    
        messages.error(request,'A ocurrido un error al eliminar el curso')
    return redirect("mantenimientoCursos")
#PARALELO
def paralelo(request):
    mensaje = definaMensajes(request)
    paralelos = Paralelo.objects.filter(estado="A")
    print("Soy el de paralelos")
    print(paralelos)
    for p in paralelos:
        print(p.paralelo)
    return render(request,'Mantenimientos/Paralelo',{
        "mensaje":mensaje,
        "paralelos":paralelos
    })

def newParalelo(request):
    try:
        if(request.method == "POST"):
            data_curso = request.POST
            obj_curso = Paralelo.objects.create(paralelo = data_curso.get('inputParalelo')
                                                ,estado="A")
            obj_curso.save()
            messages.success(request,'Paralelo creado con exito')
    except:
        messages.error(request,"A ocurrido un error al crear el curso")   
    return redirect("mantenimientoParalelos")

def deleteParalelo(request,paralelo_id):
    try:
        obj_curso = get_object_or_404(Paralelo,pk=paralelo_id)
        if(obj_curso):
            obj_curso.estado = "E"
            obj_curso.save()
            messages.success(request,'Paralelo eliminado exitosamente')
        else:
            messages.warning(request,f'El Paralelo no existe con el id {paralelo_id}')
    except:    
        messages.error(request,'A ocurrido un error al eliminar el paralelo')
    return redirect("mantenimientoParalelos")

#MATERIA
def materia(request):
    mensaje = definaMensajes(request)
    materia = Materia.objects.filter(estado="A")
    return render(request,'Mantenimientos/Materias',{
        "mensaje":mensaje,
        "materias":materia
    })
    
def newMateria(request):
    try:
        if(request.method == "POST"):
            data_materia = request.POST
            obj_materia = Materia.objects.create(materia = data_materia.get('inputMateria')
                                                ,estado="A")
            obj_materia.save()
            messages.success(request,'Materia creado con exito')
    except:
        messages.error(request,"A ocurrido un error al crear la materia")   
    return redirect("mantenimientoParalelos")

def deleteMateria(request,materia_id):
    try:
        obj_curso = get_object_or_404(Materia,pk=materia_id)
        if(obj_curso):
            obj_curso.estado = "E"
            obj_curso.save()
            messages.success(request,'Materia eliminada exitosamente')
        else:
            messages.warning(request,f'El Paralelo no existe con el id {materia_id}')
    except:    
        messages.error(request,'A ocurrido un error al eliminar el paralelo')
    return redirect("mantenimientoParalelos")

#AULA VIRTUAL
def aulaVirtual(request):
    return render(request,"Mantenimientos/AulaVirtual",{})