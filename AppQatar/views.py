from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppQatar.models import *
from AppQatar.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




def inicio(request):
      return render(request, "AppQatar/inicio.html")

def about(request):
      return render(request, 'AppQatar/about.html')

@login_required
def buscar(request):
    if request.GET["pais"]:
        pais=request.GET['pais']
        resultados=Seleccion.objects.filter(pais__icontains=pais)

        return render(request, "AppQatar/resultadosBusqueda.html",{"resultados":resultados, "busqueda":pais})

    else:
        respuesta="No enviaste datos."

    return HttpResponse(respuesta)

#REFERIDO A LA ADMINISTRACIÓN DE USUARIOS

def login_request(request):
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario=form.cleaned_data.get('username')
                  contra=form.cleaned_data.get('password')

                  user=authenticate(username=usuario, password=contra)

                  if user:
                        login(request, user)
                        return render(request, "AppQatar/inicio.html", {"mensaje": f"Has iniciado sesión como {user}"})
            else:
                  return render(request, "AppQatar/inicio.html", {"mensaje": "Datos incorrectos - Vuelve a intentarlo"})
      else:
            form = AuthenticationForm()
      
      return render(request, "AppQatar/login.html", {"form":form})


def register(request):
      if request.method == "POST":
            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  first_name=form.cleaned_data["first_name"]
                  form.save()
                  return render(request, "AppQatar/inicio.html", {"mensaje": f"{first_name}, ya sos parte del equipo!"})
      else:
            form = UserRegisterForm()
      
      return render(request, "AppQatar/registro.html", {"form":form})


@login_required
def editarPerfil(request):
      usuario = request.user

      if request.method=="POST":
            form2edit = UserEditForm(request.POST)
            if form2edit.is_valid():
                  informacion = form2edit.cleaned_data

                  usuario.first_name = informacion["first_name"]
                  usuario.last_name = informacion["last_name"]
                  usuario.email = informacion["email"]
                  usuario.set_password = informacion["password1"]
                  
                  usuario.save()

                  return render(request,"AppQatar/inicio.html")
      
      else:
            form2edit= UserEditForm(initial={
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
            "email":usuario.email
            })
      
      return render(request, "AppQatar/editarPerfil.html",{"form2edit":form2edit, "usuario":usuario})


@login_required
def addAvatar(request):
      if request.method =="POST":
            formAv = AvatarForm(request.POST, request.FILES)

            if formAv.is_valid():
                  usuarioActual= User.objects.get(username=request.user)
                  avatar= Avatar(usuario=usuarioActual, imagen=formAv.cleaned_data["imagen"])
                  avatar.save()

                  return render(request, "AppQatar/inicio.html")
      
      else:
            formAv= AvatarForm()
      
      return render(request, "AppQatar/addAvatar.html", {"formulario":formAv})



#SELECCIONES
class SeleccionList(LoginRequiredMixin, ListView):
      model=Seleccion

class SeleccionDetalle(LoginRequiredMixin, DetailView):
      model=Seleccion

class SeleccionCrear(LoginRequiredMixin, CreateView):
      model=Seleccion
      success_url= "/AppQatar/seleccion"
      fields= ["pais", "continente", "fecha","imagen2"] 

class SeleccionActualizar(LoginRequiredMixin, UpdateView):
      model=Seleccion
      success_url= "/AppQatar/seleccion"
      fields= ["pais", "continente", "fecha", "imagen2"] 

class SeleccionBorrar(LoginRequiredMixin, DeleteView):
      model=Seleccion
      success_url= "/AppQatar/seleccion"


#ESTADIOS
class EstadiosList(LoginRequiredMixin, ListView):
      model=Estadio

class EstadiosDetalle(LoginRequiredMixin, DetailView):
      model=Estadio
      success_url= "/AppQatar/estadio"

class EstadiosCrear(LoginRequiredMixin, CreateView):
      model=Estadio
      success_url= "/AppQatar/estadio"
      fields= ["nombre", "ciudad", "imagen"] 

class EstadiosActualizar(LoginRequiredMixin, UpdateView):
      model=Estadio
      success_url= "/AppQatar/estadio"
      fields= ["nombre", "ciudad", "imagen"]

class EstadiosBorrar(LoginRequiredMixin, DeleteView):
      model=Estadio
      success_url= "/AppQatar/estadio"


#COPAS
class CopasList(LoginRequiredMixin, ListView):
      model=Copas

class CopasDetalle(LoginRequiredMixin, DetailView):
      model=Copas
 
class CopasCrear(LoginRequiredMixin, CreateView):
      model=Copas
      success_url= "/AppQatar/copas"
      fields= ["selecc", "cantCopas", "ultimaCopa"] 

class CopasActualizar(LoginRequiredMixin, UpdateView):
      model=Copas
      success_url= "/AppQatar/copas"
      fields= ["selecc", "cantCopas", "ultimaCopa"] 

class CopasBorrar(LoginRequiredMixin, DeleteView):
      model=Copas
      success_url= "/AppQatar/copas"

#PREDICCIÓN
@login_required
def addPredic(request):
    if request.method == 'POST':
        miFormulario=PredForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            prediccion = Prediccion(autor=request.user, ganadora=informacion['ganadora'],
            segunda=informacion['segunda'])

            prediccion.save()

            return render(request, 'AppQatar/inicio.html')
    else:

        miFormulario=PredForm()

    return render(request, 'AppQatar/Predicciones/añadirPredicciones.html', {'form':miFormulario})


@login_required
def prediccion(request):
    prediccion = Prediccion.objects.all()

    return render(request, "AppQatar/Predicciones/listaPredicciones.html",{'resultados':prediccion})


@login_required
def borrarPredic(request, prediccion_ganadora):

    predic = Prediccion.objects.get(ganadora=prediccion_ganadora)
    
    predic.delete()
    
    prediccion = Prediccion.objects.all()

    return render(request, "AppQatar/Predicciones/listaPredicciones.html",{'resultados':prediccion})




