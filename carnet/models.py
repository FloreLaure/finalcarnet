
from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from datetime import date
from datetime import datetime
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db.models import DateTimeField
from django.utils import timezone
from django.utils.regex_helper import _lazy_re_compile
from django.utils.timezone import get_fixed_timezone
from django.contrib.auth.models import User
from django.conf import settings



class UserProfil(models.Model):
    Masculin='M'
    Feminin='F'
    choix = ((Masculin, 'Masculin'),(Feminin, 'Feminin'),)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Nom = models.CharField(max_length=30,null=True)
    Prenom = models.CharField(max_length=40, null=True)
    Profession = models.CharField(max_length=30, null=True)
    Date_de_naissance = models.DateField(default=datetime.now)
    Secteur_ou_village = models.CharField(max_length=30, null=True)
    sexe = models.CharField(max_length=6,choices=choix,default=Masculin, null=True)
    photo = models.ImageField(upload_to='upload/')
 
    def __str__(self):
        return f"{self.Date_de_naissance.strftime('%d-%m-%Y')}"

    @property
    def fileURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url
        




    
class familiaux (models.Model):
    date = models.DateField(default=datetime.now)
    famille = models.ForeignKey(User, on_delete=models.CASCADE)
    Tare = models.CharField(max_length=30)
    Prescription_Observations = models.TextField()
    Prescripteur = models.CharField(max_length=30)
    lieu = models.CharField(max_length=30, default='hopital')
    fichier = models.FileField(upload_to='upload/')

    def __str__(self):
        return f"{self.date.strftime('%d-%m-%Y')}"




class vaccinal (models.Model):
    date = models.DateField(default=datetime.now)
    vaccine = models.ForeignKey(User, on_delete=models.CASCADE)   
    Vaccin = models.CharField(max_length=30)
    Prescription_Observations = models.TextField()
    Prescripteur = models.CharField(max_length=30)
    lieu = models.CharField(max_length=30, default='hopital')
    fichier = models.FileField(upload_to='upload/')

    def __str__(self):
        return f"{self.date.strftime('%d-%m-%Y')}"


class ajouAutre (models.Model):
    date = models.DateField(default=datetime.now) 
    autr = models.ForeignKey(User, on_delete=models.CASCADE)  
    Episode_essentiels_de_maladie = models.TextField()
    Prescription_Observations = models.TextField()
    Prescripteur = models.CharField(max_length=30)
    lieu = models.CharField(max_length=30, default='hopital')
    fichier = models.FileField(upload_to='upload/')

    def __str__(self):
        return f"{self.date.strftime('%d-%m-%Y')}"





class carnetUser(models.Model):
    UserProfil = models.ForeignKey(UserProfil, on_delete=models.CASCADE)
    familiaux = models.OneToOneField(familiaux, on_delete=models.CASCADE)
    vaccinal = models.OneToOneField(vaccinal, on_delete=models.CASCADE)
    autre = models.OneToOneField(ajouAutre, on_delete=models.CASCADE)
   

