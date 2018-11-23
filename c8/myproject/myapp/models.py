from django.db import models


# Create your models here.

class Ebom(models.Model):
    ebom_name = models.CharField(max_length=200)
    date_of_addition = models.DateTimeField('date published')
    manager_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.ebom_name)


class Product(models.Model):
    ebom = models.ForeignKey(Ebom, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    date_of_addition = models.DateTimeField('date published')
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    notes = models.CharField(max_length=200)

    def __str__(self):
        return str(self.product_name)


class Additional_details_wrapper(models.Model):
    wrapper_name = models.CharField(max_length=200)
    date_of_addition = models.DateTimeField('date published')
    manager_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.wrapper_name)


class additional_product_that_are_added(models.Model):
    supply_name = models.ForeignKey(Additional_details_wrapper, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    date_of_addition = models.DateTimeField('date published')
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    notes = models.CharField(max_length=200)

    def __str__(self):
        return str(self.supply_name)


class Mbom(models.Model):
    name= models.CharField(max_length=200)
    ebom1 = models.ForeignKey(Ebom, on_delete=models.CASCADE)
    additionalDetails = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
