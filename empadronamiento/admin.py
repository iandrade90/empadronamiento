from django.contrib import admin
from .models import Person, Address, Neighborhood

admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Neighborhood)


