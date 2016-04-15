from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Personne(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(max_length=254, unique=True)
    
    def __str__(self):
        return self.prenom + ' ' + self.nom

# Create your models here.
