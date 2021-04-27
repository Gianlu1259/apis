from django.db import models

class Chela(models.Model):
    marca=models.CharField(max_length=50)
    alcohol=models.DecimalField(max_digits=4, decimal_places=2)
    militros=models.IntegerField()
    artesanal=models.BooleanField()
    nacionalidad=models.CharField(max_length=50, blank=True, null=True)
    creado=models.DateTimeField(auto_now_add=True)
    editado=models.DateTimeField(auto_now=True)
    def _str_(self):
        return self.marca

class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)