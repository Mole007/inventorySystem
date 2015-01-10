from django.contrib import admin
from main.models import country, city, bdp, mail, phone
from client.models import kindClient, client, company, area, responsible, companyContact
# Register your models here.

#--------------main---------------
admin.site.register(country)
admin.site.register(city)
admin.site.register(bdp)
admin.site.register(mail)
admin.site.register(phone)

#--------------client---------------
admin.site.register(kindClient)
admin.site.register(client)
admin.site.register(company)
admin.site.register(area)
admin.site.register(responsible)
admin.site.register(companyContact)
