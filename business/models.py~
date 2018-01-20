from django.db import models


# Район города имеет название и ID (ID автоматическое).
class District(models.Model):
    # Название. 
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

# Категория имеет название и ID (ID автоматическое).
class Category(models.Model):
    # Название.
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Enterprise_network(models.Model):
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
    #list_of_goods = models.ManyToManyField('Service')

    def __str__(self):
        return self.name

# Услуга\товар имеет название, категорию и ID (ID автоматическое).
class Service(models.Model):
    # Название.
    name = models.CharField(max_length=200)
    
    # Категория.
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    # Может продаваться в любом предприятии в сети.
   # organisation_of_mine = models.ManyToManyField(Enterprise)

    # Цена может отличаться в зависимости от предприятия.
    price = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

