from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Person(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.dni

    def get_absolute_url(self):
        return reverse('registro_direccion')

class Address(models.Model):
    calle = models.CharField(max_length=50)
    no = models.CharField(max_length=8)
    codigo_postal = models.CharField(max_length=8)
    piso = models.CharField(max_length=4, null=True, blank=True)
    departamento = models.CharField(max_length=8, null=True, blank=True)
    persona = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.calle

    def get_absolute_url(self):
        return reverse('tablero')

class Neighborhood(models.Model):
    BARRIOS_OPCIONES = (
            ('Agronomia','Agronomia'),('Almagro','Almagro'),('Balvanera','Balvanera'),
            ('Barracas','Barracas'),('Belgrano','Belgrano'),('Boedo','Boedo'),
            ('Caballito','Caballito'),('Chacarita','Chacarita'),('Coghlan','Coghlan'),
            ('Colegiales','Colegiales'),('Constitucion','Constitucion'),('Flores','Flores'),
            ('Floresta','Floresta'),('La Boca','La Boca'),('La Paternal','La Paternal'),
            ('Liniers','Liniers'),('Mataderos','Mataderos'),('Monte Castro','Monte Castro'),
            ('Monserrat','Monserrat'),('Nueva Pompeya','Nueva Pompeya'),('Nuñez','Nuñez'),
            ('Palermo','Palermo'),('Parque Avellaneda','Parque Avellaneda'),('Parque Chacabuco','Parque Chacabuco'),
            ('Parque Chas','Parque Chas'),('Parque Patricios','Parque Patricios'),('Puerto Madero','Puerto Madero'),
            ('Recoleta','Recoleta'),('Retiro','Retiro'),('Saavedra','Saavedra'),
            ('San Cristobal','San Cristobal'),('San Nicolas','San Nicolas'),('San Telmo','San Telmo'),
            ('Versalles','Versalles'),('Villa Crespo','Villa Crespo'),('Villa Devoto','Villa Devoto'),
            ('Villa General Mitre','Villa General Mitre'),('Villa Lugano','Villa Lugano'),('Villa Luro','Villa Luro'),
            ('Villa Ortuzar','Villa Ortuzar'),('Villa Pueyrredon','Villa Pueyrredon'),('Villa Real','Villa Real'),
            ('Villa Riachuelo','Villa Riachuelo'),('Villa Santa Rita','Villa Santa Rita'),('Villa Soldati','Villa Soldati'),
            ('Villa Urquiza','Villa Urquiza'),('Villa del Parque','Villa del Parque'),('Velez Sarsfield','Velez Sarsfield'))
    nombre = models.CharField(max_length=50, choices=BARRIOS_OPCIONES)
    direccion = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
