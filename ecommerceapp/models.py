from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()



# Create your models here.
class Contact(models.Model):
    # contact_id=models.AutoField(primary_key=True)

    name=models.CharField(max_length=50)
    email=models.EmailField()
    desc=models.TextField(max_length=500)
    phonenumber=models.IntegerField()
    token=models.IntegerField(default=0)

    def __int__(self):
        return self.id


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/images')

    def __str__(self):
        return self.product_name
    
class Rewards(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=50, default="")
    tokens = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/images')

    def __str__(self):
        return self.product_name

class RedeemRewards(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    hash=models.CharField(max_length=256,default='')
    email = models.CharField(max_length=90,default='')
    tokens = models.IntegerField(default=0)
    def __str__(self):
        return self.product_name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json =  models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)    
    oid=models.CharField(max_length=150,blank=True)
    amountpaid=models.CharField(max_length=500,blank=True,null=True)
    paymentstatus=models.CharField(max_length=20,blank=True)
    phone = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    delivered=models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
    
    
class Tokens(models.Model):
    email = models.CharField(max_length=90,default='')
    tokens = models.IntegerField(default=0)
    hash=models.CharField(max_length=256,default='')
    def __int__(self):
        return self.id

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
