from django.db import models

# Create your models here.

class base(models.Model):
    note = models.CharField(max_length = 255)
    create = models.DateField(auto_now_add = True)
    update = models.DateField(auto_now = True)
    
    class Meta:
        abstract = True


class brand(base):
    brand = models.CharField(max_length = 45)
    
    def __str__(self):
        return self.brand


class model(base):
    brand = models.ForeignKey(brand)
    model = models.CharField(max_length = 50)

    def __str__(self):
        return '%s - %s' %(self.brand, self.model)
    
class category(base):
category = models.CharField(max_length = 50)



create table CatArticle
(
Identification varchar(20) primary key not null,
CatModel; varchar(20) foreign key references CatModel(;Identification) on delete no action on update cascade not null,
CatCatery varchar(20) foreign key references CatCatery(Identification) on delete no action on update cascade not null,
Article varchar(30) not null,
NoSeries varchar(50) null,
CodeBar varchar(50) null,
MeasureSystem Int not null,
Presentation Int not null,
Note varchar(1000) null,
CreatedUser varchar(20)foreign key references CatUser(Identification)on delete no action on update no action not null,
UpdatedUser varchar(20)foreign key references CatUser(Identification)on delete no action on update no action not null,
CreatedDate Datetime default getdate() not null,
UpdatedDate Datetime default getdate()not null
);


create table CatCurrencyControl
(
Identification varchar(20) primary key not null,
Currency varchar(30) not null,
Simbolo varchar(5)not null,
RateChange decimal(18,6) not null,
IsPrincipal bit default 0 not null,
CreatedUser varchar(20)foreign key references CatUser(Identification)on delete no action on update no action not null,
UpdatedUser varchar(20)foreign key references CatUser(Identification)on delete no action on update no action not null,
CreatedDate Datetime default getdate() not null,
UpdatedDate Datetime default getdate()not null
);


create table TblArticlePrice
(
Identification varchar(20) primary key not null,
CatArticle varchar(20) foreign key references CatArticle(Identification)on delete no action on update cascade not null,
Price decimal(18,8) not null,
IsActive bit default 1 not null,
CreatedUser varchar(20)foreign key references CatUser(Identification)on delete no action on update no action not null,
UpdatedUser varchar(20)foreign key references CatUser(Identification)on delete no action on update no action not null,
CreatedDate Datetime default getdate() not null,
UpdatedDate Datetime default getdate()not null
);