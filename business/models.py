from django.db import models


class City_region(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Enterprise_network(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Enterprise(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    enterprise_network = models.ForeignKey(Enterprise_network, on_delete=models.CASCADE)    
    city_region = models.ManyToManyField(City_region)  
    services_list = []

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    enterprise = models.ManyToManyField(Enterprise)

    def __str__(self):
        return self.name

