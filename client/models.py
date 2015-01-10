from django.db import models
from main.models import bdp

# Create your models here.

class base(models.Model):
    note = models.CharField(max_length = 255, null = True, blank = True)
    create = models.DateField(auto_now_add = True)
    update = models.DateField(auto_now = True)
    
    class Meta:
        abstract = True

        
class kindClient(base):
    kind = models.CharField(max_length = 35)
    credictTime = models.IntegerField(default = 15)
    credictMax = models.FloatField() #maximo de credito --- es 0.0 -- revision
    discount = models.FloatField() # definir un porcentage de descuento --- es 0.0 --- revision
    
    def __str__(self):
        return self.kind
    
    
class client(bdp):
    GENDER_LIST = ((1,'Hombre'),(2,'Mujer'),(3,'Otro')) 
    gender = models.IntegerField(choices = GENDER_LIST)
    
    
class company(bdp):
    CKIND_LIST = ((1,'Privada'),(2,'Publica'),(3,'Mixta')) 
    kind = models.IntegerField(choices = CKIND_LIST)
    
class area(base):
    area = models.CharField(max_length = 45)
    
    def __str__(self):
        return self.area
    
    
class responsible(base):
    area = models.ForeignKey(area)
    responsible = models.CharField(max_length = 45)
    company = models.ManyToManyField(company, through = 'companyContact')
    
    def __str__(self):
        return '%s - %s' %(self.responsible, self.area)
    
    
class companyContact(bdp): #contacto cliente - otros contacto (recursividad)
    company = models.ForeignKey(company)
    responsible = models.ForeignKey(responsible)
    GENDER_LIST = ((1,'Hombre'),(2,'Mujer'),(3,'Otro')) 
    gender = models.IntegerField(choices = GENDER_LIST)

    
    
