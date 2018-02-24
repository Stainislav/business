from django.db import models


# Район города имеет название и ID (ID автоматическое).
class District(models.Model):

    # Название. 
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Район города"
        verbose_name_plural = "Районы города"

# Категория имеет название и ID (ID автоматическое).
class Category(models.Model):
    
    # Название.
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Enterprise_network(models.Model):
    
    # Название.
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Предприятие имеет название, описание и ID (ID автоматическое).
class Organisation(models.Model):

    # Название.
    name = models.CharField(max_length=200)

    # Описание.
    description = models.CharField(max_length=200)

    # Принадлежит одной из сети предприятий. 
    enterprise_network = models.ForeignKey(Enterprise_network, on_delete=models.CASCADE)    

    # Имеет принадлежность к нескольким районам города, может быть представлена сразу в нескольких.
    city_region = models.ManyToManyField(District)  

    # Имеет список предоставляемых услуг\товаров с ценами.
    goods = models.ManyToManyField('Service', through='Membership')
    
    def __str__(self):
        return self.name

            
# Услуга\товар имеет название, категорию и ID (ID автоматическое).
class Service(models.Model):

    # Название.
    name = models.CharField(max_length=200)
    
    # Категория.
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name


class Membership(models.Model):

    # Может продаваться в любом предприятии в сети.
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    
    # Цена может отличаться в зависимости от предприятия.
    price = models.CharField(max_length=200)

