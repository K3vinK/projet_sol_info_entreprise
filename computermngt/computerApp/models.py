from pyexpat import model
from django.db import models
from datetime import datetime

class Machine(models.Model):

    TYPE = (
        ('PC', ('PC - Run Windows')),
        ('MAC', ('MAC - Run MacOS')),
        ('Serveur', ('Serveur Simple server to deploy Run Windows')),
        ('Switch', ('Switch to maintain and connects servers')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=6)
    maintenanceDate = models.DateField(default = datetime.now())
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')

class Personne(models.Model):
    id = models.AutoField(
                    primary_key=True,
                    editable=False)
    prenom = models.CharField(
                max_length= 6)  
    nom = models.CharField(
                max_length= 6)                  

    def __str__ (self):
        return str(self.id) + " -> " + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom

class get_object_or_404(models.Model):
    id = models.AutoField(
                    primary_key=True,
                    editable=False)
    prenom = models.CharField(
                max_length= 6)  
    nom = models.CharField(
                max_length= 6)                  

    def __str__ (self):
        return str(self.id) + " -> " + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom