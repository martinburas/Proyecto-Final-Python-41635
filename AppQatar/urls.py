from django.urls import path

from AppQatar import views
from AppQatar.views import *





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    #path('seleccion', views.seleccion, name="Seleccion"),
    #path('estadio', views.estadio, name="Estadio"),
    #path('copas', views.copas, name="Copas"),
    #path('buscar/', views.buscar),
    #path('leerSeleccion', views.leerSeleccion, name='LeerSeleccion'),
    #path('eliminarSeleccion/<seleccion_pais>', views.eliminarSeleccion, name='EliminarSeleccion'),
    #path('editarSeleccion/<seleccion_pais>', views.editarSeleccion, name='EditarSeleccion'),
    
    path('login', login_request, name="Login"),
    path('register', register, name="Registro"),
    path('logout', LogoutView.as_view(template_name='AppQatar/logout.html'), name="Logout"),
    path('editarPerfil', editarPerfil, name="EditarPerfil"),
    path('addAvatar', addAvatar, name="addAvatar"),
    path('about', views.about, name='Acerca de mí'),
    path('buscar/', views.buscar),

    path('seleccion', SeleccionList.as_view(), name="Selecciones"),
    path('seleccion/<int:pk>', SeleccionDetalle.as_view(), name="SeleccionDetalle"),
    path('seleccion/crear/', SeleccionCrear.as_view(), name="SeleccionCrear"),
    path('seleccion/editar/<int:pk>', SeleccionActualizar.as_view(), name="SeleccionActualizar"),
    path('seleccion/eliminar/<int:pk>', SeleccionBorrar.as_view(), name="SeleccionBorrar"),

    path('estadio', EstadiosList.as_view(), name="Estadio"),
    path('estadio/<int:pk>', EstadiosDetalle.as_view(), name="EstadiosDetalle"),
    path('estadio/crear/', EstadiosCrear.as_view(), name="EstadiosCrear"),
    path('estadio/editar/<int:pk>', EstadiosActualizar.as_view(), name="EstadiosActualizar"),
    path('estadio/eliminar/<int:pk>', EstadiosBorrar.as_view(), name="EstadiosBorrar"),

    path('copas', CopasList.as_view(), name="Copas"),
    path('copas/<int:pk>', CopasDetalle.as_view(), name="CopasDetalle"),
    path('copas/crear/', CopasCrear.as_view(), name="CopasCrear"),
    path('copas/editar/<int:pk>', CopasActualizar.as_view(), name="CopasActualizar"),
    path('copas/eliminar/<int:pk>', CopasBorrar.as_view(), name="CopasBorrar"),

    path('addPrediccion',views.addPredic, name='Añadir Prediccion'),
    path('Predicciones', views.prediccion, name='Predicciones'),

]
