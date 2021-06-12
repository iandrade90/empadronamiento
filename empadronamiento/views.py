from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Person, Address
from django.contrib.auth.models import User
from .forms import PersonForm, AddressForm

class CreatePerson(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['nombre', 'apellido', 'dni']
    template_name = 'registro_persona.html'

    def form_valid(self, form):
        form.instance.usuario_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('registro_direccion')

class UpdatePerson(LoginRequiredMixin, View):
    template_name = 'modificar_persona.html'
    
    def post(self, request, p_id):
        persona = Person.objects.get(usuario_id=p_id)
        if request.method == 'POST':
            personForm = PersonForm(request.POST, instance=persona)
            if personForm.is_valid():
                personForm.save()
                return redirect('tablero')

    def get(self,request, p_id):
        persona = Person.objects.get(usuario_id=p_id)
        personForm = PersonForm(instance=persona)
        context = {'personForm': personForm}
        return render(request, self.template_name, context)


class CreateAddress(LoginRequiredMixin, CreateView):
    model = Address
    fields = ['calle', 'no', 'codigo_postal', 'piso', 'departamento', 'barrio'] 
    template_name = 'registro_direccion.html'

    def form_valid(self, form):
        form.instance.persona_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tablero')

class UpdateAddress(LoginRequiredMixin, View):
    template_name = 'modificar_direccion.html'

    def post(self, request, p_id):
        direccion = Address.objects.get(persona_id=p_id)
        if request.method == 'POST':
            addressForm = AddressForm(request.POST, instance=direccion)
            if addressForm.is_valid():
                addressForm.save()
                return redirect('tablero')

    def get(self, request, p_id):
        direccion = Address.objects.get(persona_id=p_id)
        addressForm = AddressForm(instance=direccion)
        context = {'addressForm': addressForm}
        return render(request, self.template_name, context)

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
        if Address.objects.filter(persona_id=p_id).exists():
            direccion = Address.objects.get(persona_id=p_id)
            detalle = {'direccion':direccion}
            return render(request, self.template_name, detalle)
        else:
            return redirect('sin_direccion')
