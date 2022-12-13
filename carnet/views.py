from django.shortcuts import render,redirect
from urllib import request, response
from django.http import HttpResponse, HttpResponseRedirect   # pass view information into the browser
from carnet.models import User, familiaux,UserProfil, vaccinal, ajouAutre, carnetUser # import the models from polls/models.py
from django.contrib import messages
from . import forms
from carnet.forms import CompteForm,loginForm, ajoutAutreForm, ajoutFamiliauxForm, ajoutVaccinalForm,LoginUserView,carnetUserForm,UserForm, UserProfileForm# import the models from polls/models.py

from django.contrib.auth import authenticate,logout,login

from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

from django.urls import reverse_lazy
from django.views.generic import TemplateView

from django.contrib.auth.hashers import make_password

import re






## La vue index pour la page d'accueil

def index(request):
    context = {
        'page_title' : "accueil",
    }
    return render(request, 'index.html', context)



# la vue sante pour la page de connexion, là ou on accède au carnet




def Voirvaccinal(request):
    vaccinale = vaccinal.objects.filter(vaccine_id=request.user.pk)  
    return render(request,"vaccinal.html",{'vaccinale':vaccinale})  



# la vue autre prsente les autres antécedants ( consultation et autre)

def Voirautre(request):
    autes = ajouAutre.objects.filter(autr_id=request.user.pk)  
    return render(request,"autre.html",{'autres':autres})  



# la vue familiaux présente les antécédents familiaux du User

def Voirfamiliaux(request):
    familiau = familiaux.objects.filter(famille_id=request.user.pk)  
    return render(request,"familiaux.html",{'familiau':familiau})  

## fin antécedant




## début mise à jour du carnet

## la vue ajoufamiliaux permet au personnel soignant d'ajouter de nouvelles information sur les antécédent familiaux du User

def antecedantFamiliaux(request):
    form = ajoutFamiliauxForm()
    if request.method == "POST":
        date = request.POST.get('date')
        Tare = request.POST.get('Tare')
        Prescription_Observations = request.POST.get('Prescription_Observations')
        Prescripteur = request.POST.get('Prescripteur')
        lieu = request.POST.get('lieu')
        fichier = request.POST.get('fichier')
        famille=request.user

        donnee = familiaux.objects.create(date=date, Tare=Tare, Prescription_Observations=Prescription_Observations,
        Prescripteur=Prescripteur, lieu=lieu, fichier=fichier,famille=famille)

        donnee.save()
        return redirect('familiaux')
    else:
        return render(request, 'ajoufamiliaux.html', {'form':form})





## la vue ajouvaccin permet au personnel soignant d'ajouter de nouvelles information sur les antécédent vaccinal du User (nouvelle vaccinations)


def antecedantVaccin(request):
    form=ajoutVaccinalForm()
    if request.method == "POST":
        date = request.POST.get('date')
        Vaccin = request.POST.get('Vaccin')
        Prescription_Observations = request.POST.get('Prescription_Observations')
        Prescripteur = request.POST.get('Prescripteur')
        lieu = request.POST.get('lieu')
        fichier = request.POST.get('fichier')
        vaccine = request.user


        donnee = vaccinal.objects.create(date=date, Vaccin=Vaccin, Prescription_Observations=Prescription_Observations,
        Prescripteur=Prescripteur, lieu=lieu, fichier=fichier, vaccine=vaccine)

        donnee.save()
        return redirect('vaccinal')
    else:
        return render(request, 'ajouvaccin.html', {'form':form})







## la vue ajouAutre permet au personnel soignant d'ajouter de nouvelles information sur la santé du User(nouvelle consultation et autre)

def ajouAntecedant(request):

    form = ajoutAutreForm()
    if request.method == "POST":
        date = request.POST.get('date')
        Episode_essentiels_de_maladie = request.POST.get('Episode_essentiels_de_maladie')
        Prescription_Observations = request.POST.get('Prescription_Observations')
        Prescripteur = request.POST.get('Prescripteur')
        lieu = request.POST.get('lieu')
        fichier = request.POST.get('fichier')
        autr=request.user

        donnee = ajouAutre.objects.create(date=date, Episode_essentiels_de_maladie=Episode_essentiels_de_maladie, Prescription_Observations=Prescription_Observations,
        Prescripteur=Prescripteur, lieu=lieu, fichier=fichier,autr=autr)

        donnee.save()
        return redirect('autre')
    else:
        return render(request, 'ajoutAutre.html', {'form':form})




def show(request):  
    autres = autre.objects.all()  
    return render(request,"carnet.html",{'autres':autres})  


def edit(request, id):  
    autr = autre.objects.get(id=id)  
    return render(request,'ajoutAutre.html', {'autr':autr}) 

 
def update(request, id): 
    autr = autre.objects.get(id=id)  
    form = ajoutAutreForm(request.POST, instance = autr)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'ajoutAutre.html', {'autr': autr})   

    
## fin mise à jour du carnet




## la vue Compte pour la création des comptes




def Compte(request):
    form = forms.CompteForm()
    if request.method=='POST':
        form = forms.CompteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
    return render(request,'compte.html', {"form":form})



def Carnet(request):
    carnet = UserProfil.objects.get(user_id=request.user.pk)
    context = {"page_title":"Sante", "carnet":carnet}
    return render(request, 'carnet.html', context)    



def sante(request):
    form = carnetUserForm()
    if request.method == "POST":
        Nom = request.POST.get('Nom')
        Prenom = request.POST.get('Prenom')
        Date_de_naissance = request.POST.get('Date_de_naissance')
        Profession = request.POST.get('Profession')
        Secteur_ou_village = request.POST.get('Secteur_ou_village')
        sexe = request.POST.get('sexe')
        photo = request.POST.get('photo')
        user = request.user
        
        donnee = UserProfil.objects.create(Nom=Nom, Prenom=Prenom, Date_de_naissance=Date_de_naissance,
        Profession=Profession, Secteur_ou_village=Secteur_ou_village, sexe=sexe, photo=photo, user=user)

        donnee.save()

        return redirect ('Carnet')

    else:
       return render(request, 'obtien_carnet.html', {'form':form})



def LoginView(request):
    if request.method == 'POST':

        username = request.POST.get['username']
        password = request.POST.get['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sante')
        else:
            return redirect('login')
    else:
        return redirect('login')



def LogoutView(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html', context)

            ...
        else:
            print("---ERRORS---", form.errors, form_profile.errors)
            ...
    else:
        return render(request, 'index.html', context)
