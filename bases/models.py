from django.db import models
from django.contrib.auth.models import User


#tipo de datos 
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True) # herencia de modelo 
    fc = models.DateTimeField(auto_now=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True,null=True)


    class Meta:
        abstract=True
# Create your models here.
