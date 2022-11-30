
from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from datetime import date
from datetime import datetime
#django.utils.timezone.now 

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from django.db.models import DateTimeField
from django.utils import timezone

from django.utils.regex_helper import _lazy_re_compile
from django.utils.timezone import get_fixed_timezone


from django.contrib.auth.models import User, AbstractUser,AbstractBaseUser

from django.conf import settings


class User (User):
   pass


    
class familiaux (models.Model):
    date = models.DateField(default=datetime.now)
    Tare = models.CharField(max_length=30)
    Prescription_Observations = models.TextField()
    Prescripteur = models.CharField(max_length=30)
    lieu = models.CharField(max_length=30, default='hopital')
    fichier = models.FileField()

    def __str__(self):
        return f"{self.date.strftime('%d-%m-%Y')}"




class vaccinal (models.Model):
    date = models.DateField(default=datetime.now)   
    Vaccin = models.CharField(max_length=30)
    Prescription_Observations = models.TextField()
    Prescripteur = models.CharField(max_length=30)
    lieu = models.CharField(max_length=30, default='hopital')
    fichier = models.FileField()

    def __str__(self):
        return f"{self.date.strftime('%d-%m-%Y')}"


class autre (models.Model):
    date = models.DateField(default=datetime.now)   
    Episode_essentiels_de_maladie = models.TextField()
    Prescription_Observations = models.TextField()
    Prescripteur = models.CharField(max_length=30)
    lieu = models.CharField(max_length=30, default='hopital')
    fichier = models.FileField()

    def __str__(self):
        return f"{self.date.strftime('%d-%m-%Y')}"



        # proprietaire = models.ForeignKey(User, on_delete=models.CASCADE, db_column="password1", blank=True )



class UserProfil(models.Model):
    Masculin='M'
    Feminin='F'
    choix = ((Masculin, 'Masculin'),(Feminin, 'Feminin'),)

    Nom = models.CharField(max_length=30,null=True)
    Prenom = models.CharField(max_length=40, null=True)
    Profession = models.CharField(max_length=30, null=True)
    Date_de_naissance = models.DateField(default=datetime.now)
    Secteur_ou_village = models.CharField(max_length=30, null=True)
    sexe = models.CharField(max_length=6,choices=choix,default=Masculin, null=True)
    photo = models.ImageField(upload_to='upload/')
    person = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"{self.Date_de_naissance.strftime('%d-%m-%Y')}"


class carnetUser(models.Model):
    UserProfil = models.OneToOneField(
        UserProfil,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    familiaux = models.OneToOneField(familiaux,
        on_delete=models.CASCADE,
    )
    vaccinal = models.OneToOneField(
        vaccinal,
        on_delete=models.CASCADE,
    )
    autre = models.OneToOneField(
        autre,
        on_delete=models.CASCADE,
    )
   

