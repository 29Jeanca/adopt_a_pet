from django.db import models
from django.forms import ValidationError

# Create your models here.
class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.name:
            raise ValidationError('Ingrese un nombre. EL NOMBRE NO PUEDE ESTAR VACÍO')
        
        if not self.email:
            raise ValidationError('Ingrese un nombre. EL email NO PUEDE ESTAR VACÍO')
        
        if not self.age:
            raise ValidationError('Ingrese un nombre. La edad NO PUEDE ESTAR VACÍA')
        

    def pets_adopted_count(self):
        return self.pets.count()
    
    def pets_names(self):
        return ", ".join([pet.name for pet in self.pets.all()])
    

    
    def __str__(self) -> str:
        return self.name
    
class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    color = models.CharField(max_length=100)
    weight = models.FloatField()
    species = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.age

class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE,related_name="pets")
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE,related_name="pets")
    adoption_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
    

