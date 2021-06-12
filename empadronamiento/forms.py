from django.forms import ModelForm
from .models import Person, Address

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['nombre', 'apellido', 'dni']

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['calle', 'no', 'codigo_postal', 'piso', 'departamento', 'barrio']
