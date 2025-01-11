from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='static/images')
    def __str__(self):
        return self.username


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    customer_business_name=models.CharField(max_length=20)
    customer_business_address=models.CharField(max_length=200)
    customer_business_phone=models.CharField(max_length=11)
    customer_business_email=models.EmailField()
    customer_business_photo=models.ImageField(upload_to='static/images')
    def __str__(self):
        return self.username
    
    