from django.forms import ModelForm
from .models import Person, Neighborhood, Address

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['fname', 'lname', 'dni']
