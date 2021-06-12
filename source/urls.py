"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView
from empadronamiento.views import (
        CreatePerson, 
        CreateAddress, 
        DetailAddressView, 
        DetailPersonView,
        UpdatePerson,
        UpdateAddress)
from login.views import login, register, homePage, profile, dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='index'), 
    path('nuevo_registro/', register, name='registro'),
    path('iniciar_sesion/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('sesion_finalizada/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('tablero/', dashboard, name='tablero'),
    path('tablero/info_personal/<int:p_id>/', DetailPersonView.as_view(), name='info'),
    path('tablero/info_personal/info_direccion/<int:p_id>/', DetailAddressView.as_view(), name='direccion'),
    path('tablero/sin_registros/', TemplateView.as_view(template_name='no_registro.html'), name='sin_registros'),
    path('tablero/sin_direccion/', TemplateView.as_view(template_name='no_direccion.html'), name='sin_direccion'),
    path('tablero/perfil/', profile, name='perfil'),
    path('tablero/registro_persona/', CreatePerson.as_view(), name='registro_persona'),
    path('tablero/registro_direccion/', CreateAddress.as_view(), name='registro_direccion'),
    path('tablero/modificar_info_personal/<int:p_id>', UpdatePerson.as_view(), name='modificar_info_personal'),
    path('tablero/modificar_direccion/<int:p_id>', UpdateAddress.as_view(), name='modificar_direccion'),
]
