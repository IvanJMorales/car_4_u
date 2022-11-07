from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    make = models.CharField(max_length=200, null=True, blank=True)
    year = models.IntegerField( null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=0, null=True, blank=True)
    miles = models.IntegerField( null=True, blank=True)
    engine = models.CharField(max_length=200, null=True, blank=True, default=0)
    link = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,  upload_to='images/')
    #description = models.TextField(null=True, blank=True)
    #createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
