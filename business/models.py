from django.db import models


# Район города.
class District(models.Model): 
    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Район города"
        verbose_name_plural = "Районы города"


# Категория.
class Category(models.Model):
    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# Сеть предприятий.
class Enterprise_network(models.Model):
    
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сеть предприятий"
        verbose_name_plural = "Сети предприятий"


# Предприятие.
class Organisation(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200) 
    organization_network = models.ForeignKey(Enterprise_network, on_delete=models.CASCADE)    
    district = models.ManyToManyField(District)  

    goods = models.ManyToManyField('Service', through='Membership')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"

            
# Услуга.
class Service(models.Model):

    name = models.CharField(max_length=200)
    
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


# Связь 'товар-цена'
class Membership(models.Model):

    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    
    price = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Связь 'товар-цена'"
        verbose_name_plural = "Связи 'товар-цена'"

    def __str__(self):
        return "Товар: %s Предприятие: %s" % (self.service.name, self.organisation.name)
