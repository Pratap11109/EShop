from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    cho=[('ele','Electronic'),('mobile','Mobile'),('laptop','LapTop'),('mw','MansWear')]
    p_name = models.CharField(max_length=50)
    p_countity = models.IntegerField()
    p_price = models.IntegerField()
    p_dis =models.TextField()
    p_img = models.ImageField(upload_to='Product')
    cat = models.CharField(max_length=50,choices=cho)
    Supplier = models.ForeignKey(User,on_delete=models.CASCADE)


class OrderDetails(models.Model):
    product =models.ForeignKey(Product , on_delete=models.CASCADE)
    qut = models.IntegerField()
    OrderDate= models.DateField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey( User , on_delete=models.CASCADE)



class Addres(models.Model):
    Addrese=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Order(models.Model):
    add = models.ForeignKey(Addres,on_delete=models.CASCADE)
    OD= models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    deliverydate= models.DateField(auto_now=False, auto_now_add=False)
    totalpayment=models.IntegerField()



class Payment(models.Model):
    order=models.ForeignKey( Order , on_delete=models.CASCADE)
    payp = models.IntegerField()
    payrem = models.IntegerField()
   
