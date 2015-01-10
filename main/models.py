from django.db import models
from client.models import client, company
# Create your models here.
    
class base(models.Model):
    note = models.CharField(max_length = 255, null = True, blank = True)
    create = models.DateField(auto_now_add = True)
    update = models.DateField(auto_now = True)
    
    class Meta:
        abstract = True

        
class country(base):
    country = models.CharField(max_length = 75)
    
    def __str__(self):
        return self.country

    
class city(base):
    contry = models.ForeignKey(country)
    city = models.CharField(max_length = 65)
    
    def __str__(self):
        return self.city
    

class bdp(base):
    numIdCard = models.CharField(max_length = 20) #kind unique
    photo = models.CharField(max_length = 250, null = True, blank = True)
    name = models.CharField(max_length = 35) #Company name 
    surname = models.CharField(max_length = 35) #Social Name
    birthdate = models.DateField()
    city = models.ForeignKey(city)
    address = models.CharField(max_length = 250, null = True, blank = True)
    
    def __str__(self):
        return '%s - %s' %(self.name, self.surname)

    
    
class mail(base):
    bdp = models.ForeignKey(bdp)
    KMAIL_LIST = ((1,'Private'),(2,'Public'),(3,'Coorporative')) 
    kind = models.IntegerField(choices = KMAIL_LIST)
    mail = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.mail

    

class phone(base):
    bdp = models.ForeignKey(bdp)
    KPHONE_LIST = ((1,'Mobil'),(2,'Home'),(3,'Coorporative')) 
    kind = models.IntegerField(choices = KPHONE_LIST)
    code = models.IntegerField(null = True, blank = True)
    area = models.IntegerField(null = True, blank = True)
    phone = models.IntegerField()
    
    def _get_phone_number_(self):
        return '%s - (%s) - %s' %(self.code, self.area, self.phone)
    
    get_phone = property(_get_phone_number_)

    
class bill_client (base):
    date = models.DateField()
    number = models.IntegerField()
    client = models.ForeignKey(client)

        
class bill_company(base):
    date = models.DateField()
    number = models.IntegerField()
    company = models.ForeignKey(company)
    datevencimiento = models.DateField()
    payDate = models.DateField()
    depositnumber = models.IntegerField() #check
    STATE_LIST = ((1,'Pagado'),(2,'Debe'),(3,'Abonado'),(4,'Nulo'))
    state = models.IntegerField(choices = STATE_LIST) #check to a TinyInt 
    

    
 
    

    

    