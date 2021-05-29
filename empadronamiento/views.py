from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Person, Address, Neighborhood
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class CreatePerson(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['nombre', 'apellido', 'dni']
    template_name = 'registro_persona.html'

    def form_valid(self, form):
        form.instance.usuario_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('registro_direccion')

class CreateAddress(LoginRequiredMixin, CreateView):
    model = Address
    fields = ['calle', 'no', 'codigo_postal', 'piso', 'departamento'] 
    template_name = 'registro_direccion.html'

    def form_valid(self, form):
        form.instance.persona_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('registro_barrio')

class CreateNeighborhood(LoginRequiredMixin, CreateView):
    model = Neighborhood
    fields = ['nombre']
    template_name = 'registro_barrio.html'

    def form_valid(self, form):
        form.instance.direccion_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tablero')

class DetailPersonView(LoginRequiredMixin, View):
    template_name = 'info_usuario.html'

    def get(self, request, p_id):
        if Person.objects.filter(usuario_id=p_id).exists():
            persona = Person.objects.get(usuario_id=p_id)
            detalle = {'persona': persona}
            return render(request, self.template_name, detalle)
        else:
            return redirect('sin_registros')

class DetailAddressView(LoginRequiredMixin, View):
    template_name = 'info_direccion.html'

    def get(self, request, p_id):
        if Address.objects.filter(persona_id=p_id).exists() and Neighborhood.objects.filter(direccion_id=p_id).exists():
            direccion = Address.objects.get(persona_id=p_id)
            barrio = Neighborhood.objects.get(direccion_id=p_id)
            detalle = {'direccion':direccion,'barrio':barrio}
            return render(request, self.template_name, detalle)
        else:
            return redirect('sin_direccion')
