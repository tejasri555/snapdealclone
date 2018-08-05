from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobileno = models.CharField(max_length=30, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Address(models.Model):
    country=models.CharField(max_length=20)
    fullname=models.CharField(max_length=64)
    mobileno=models.CharField(max_length=30, blank=True)
    pincode=models.CharField(max_length=10)
    street=models.CharField(max_length=200)
    landmark=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    address_type=models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def  __str__(self):
        return self.fullname

class Category(models.Model):
    title = models.CharField(max_length=200)
    active= models.BooleanField(default=True)
    image = models.ImageField(upload_to='products', null=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

# class Subcategory(models.Model):
#     title = models.CharField(max_length=200)
#     active = models.BooleanField(default=True)
#     image = models.ImageField(upload_to='products', null=True)
#     description = models.CharField(max_length=500)
#     category=models.ForeignKey(Category,on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    rating= models.IntegerField()
    units = models.IntegerField()
    image=models.ImageField(upload_to='products', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



    def __str__(self):
        return self.title



class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    products= models.ForeignKey(Product, blank=True,on_delete=models.CASCADE)
    subtotal= models.DecimalField(default=0.00, max_digits=50, decimal_places=2)
    image = models.ImageField(blank=True, null=True, upload_to="products/")
    quantity = models.IntegerField()


class OrderedItems(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    products= models.ForeignKey(Product, blank=True,on_delete=models.CASCADE)
    subtotal= models.DecimalField(default=0.00, max_digits=50, decimal_places=2)
    image = models.ImageField(blank=True, null=True, upload_to="products/")
    quantity = models.IntegerField()



