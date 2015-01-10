from django.db import models
from main.models import bdp
from client.models import responsible

# Create your models here.

class base(models.Model):
    note = models.CharField(max_length = 255)
    create = models.DateField(auto_now_add = True)
    update = models.DateField(auto_now = True)
    
    class Meta:
        abstract = True
   

class companySeller(bdp): #Vendedor Asignado (recursividad)
    responsible = models.ForeignKey(responsible)
    GENDER_LIST = ((1,'Hombre'),(2,'Mujer'),(3,'Otro')) 
    gender = models.IntegerField(choices = GENDER_LIST)
    isActice = models.BooleanField(default=True)
    parent = models.IntegerField(default = 0) #---->Recursividad Se pone el ID del Venderdor al que apoya - cuando no apoya a ninguna su valor es 0 (valor por defecto) solo se cambia cuando se asigna un ID      