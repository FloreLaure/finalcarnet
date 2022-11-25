from django.shortcuts import render,redirect
from urllib import request, response
from django.http import HttpResponse, HttpResponseRedirect   # pass view information into the browser
from carnet.models import User, familiaux, vaccinal, autre, Carnet_user,UserProfile # import the models from polls/models.py
from django.contrib import messages
# from .forms import CompteForm
from carnet.forms import CompteForm,CarnetForm,loginForm, ajoutAutreForm, ajoutFamiliauxForm, ajoutVaccinalForm,LoginUserView,UserProfileForm,UserForm # import the models from polls/models.py

from django.contrib.auth import authenticate,logout,login

from django.contrib.auth.forms import UserCreationForm

# authentication/views.py
from django.conf import settings

from django.urls import reverse_lazy
from django.views.generic import TemplateView





## La vue index pour la page d'accueil

def index(request):
    context = {
        'page_title' : "accueil",
    }
    return render(request, 'index.html', context)



# la vue sante pour la page de connexion, là ou on accède au carnet


def vaccinal(request):

    context = {
        'page_title' : 'vaccin',
        'vaccin' : vaccin
    }
    return render(request, 'vaccinal.html', context)



# la vue autre prsente les autres antécedants ( consultation et autre)

def autre(request):

    context = {
        'page_title' : "Sante",
        'autre' : autr
    }
    return render(request, 'autre.html', context)    



# la vue familiaux présente les antécédents familiaux du User

def familiaux(request):

    context = {
        'page_title' : "Sante",
        'familiaux' : famille,    
    }

    return render(request, 'familiaux.html', context)    

## fin antécedant




## début mise à jour du carnet

## la vue ajoufamiliaux permet au personnel soignant d'ajouter de nouvelles information sur les antécédent familiaux du User

def ajoufamiliaux(request):
    form = ajoutFamiliauxForm()
    if request.method == "POST":
        date = request.POST.get('date')
        tare = request.POST.get('tare')
        Prescription_Observations = request.POST.get('Prescription_Observations')
        Prescripteur = request.POST.get('Prescripteur')
        lieu = request.POST.get('lieu')
        fichier = request.POST.get('fichier')

        donnee = Carnet_user.objects.create(date=date, tare=tare, Prescription_Observations=Prescription_Observations,
        Prescripteur=Prescripteur, lieu=lieu, fichier=fichier)


        donnee.save()


        return render(request, 'familiaux.html', {'form':form})

    else:
        return render(request, 'ajoufamiliaux.html', {'form':form})




## la vue ajouvaccin permet au personnel soignant d'ajouter de nouvelles information sur les antécédent vaccinal du User (nouvelle vaccinations)


def ajouvaccin(request):
    form=ajoutVaccinalForm()
    if request.method == "POST":
        date = request.POST.get('date')
        dose = request.POST.get('dose')
        Prescription_Observations = request.POST.get('Prescription_Observations')
        Prescripteur = request.POST.get('Prescripteur')
        lieu = request.POST.get('lieu')
        fichier = request.POST.get('fichier')

        donnee = Carnet_user.objects.create(date=date, dose=dose, Prescription_Observations=Prescription_Observations,
        Prescripteur=Prescripteur, lieu=lieu, fichier=fichier)


        donnee.save()


        return render(request, 'vaccinal.html', {'form':form})

    else:
        return render(request, 'ajouvaccin.html', {'form':form})







## la vue ajouAutre permet au personnel soignant d'ajouter de nouvelles information sur la santé du User(nouvelle consultation et autre)

def ajouAutre(request):
    form = ajoutAutreForm()
    if request.method == "POST":
        date = request.POST.get('date')
        Episode_essentiels_de_maladie = request.POST.get('Episode_essentiels_de_maladie')
        Prescription_Observations = request.POST.get('Prescription_Observations')
        Prescripteur = request.POST.get('Prescripteur')
        lieu = request.POST.get('lieu')
        fichier = request.POST.get('fichier')

        donnee = Carnet_user.objects.create(date=date, Episode_essentiels_de_maladie=Episode_essentiels_de_maladie, Prescription_Observations=Prescription_Observations,
        Prescripteur=Prescripteur, lieu=lieu, fichier=fichier)


        donnee.save()


        return render(request, 'autre.html', {'form':form})

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
    form = CompteForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        donnee = User.objects.create(username=username, password1=password1, password2=password2)


        donnee.save()        
        return redirect('login')
    else:
        return render(request, 'compte.html', {"form":form})
       



def Carnet(request):
    form = CarnetForm()
    if request.method == "POST":
        Nom = request.POST.get('Nom')
        Prenom = request.POST.get('Prenom')
        Date_de_naissance = request.POST.get('Date_de_naissance')
        Profession = request.POST.get('Profession')
        Secteur_ou_village = request.POST.get('Secteur_ou_village')
        sexe = request.POST.get('sexe')
        photo = request.POST.get('photo')
        


        donnee = Carnet_user.objects.create(Nom=Nom, Prenom=Prenom, Date_de_naissance=Date_de_naissance,
        Profession=Profession, Secteur_ou_village=Secteur_ou_village, sexe=sexe, photo=photo)


        donnee.save()


        return render(request, 'carnet.html', {'form':form})

    else:
        return render(request, 'obtien_carnet.html', {'form':form})



def sante(request):
    proprietaire = Carnet_user.objects.select_related("User").all().filter(id=id)

    context = {
        'user' : proprietaire
        } 

    return render(request, 'carnet.html', context)









def LoginView(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        form_profile = CompteForm(request.POST)
      
        print("data", form.data)

        if form.is_valid() and form_profile.is_valid():
            user = form.save()
            profile = form_profile.save(commit=False)
            profile.user = user # the user has to be saved before the profile
            form_profile.save()
            num=num+1
            if num==1:
                return redirect('login')
            else:   
                return render(request, 'carnet.html', context)
        else:
            print("---ERRORS---", form.errors, form_profile.errors)
            context['forms'] = [form, form_profile]
            return render(request, 'compte.html', context)

    else:
             # GET, generate blank form
        context['forms'] = [UserForm(),CompteForm()]
        return render(request, 'compte.html', context)


       



def LogoutView(request):
    username = request.POST.get['username']
    password = request.POST.get['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'index.html', context)

        # Redirect to a success page.
        ...
    else:
        print("---ERRORS---", form.errors, form_profile.errors)
        # Return an 'invalid login' error message.
        ...





# def inde(request):
#     context = {
#         'page_title' : "Homepage",
#     }

#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         form_profile = UserProfileForm(request.POST)

#         print("data", form.data)

#         if form.is_valid() and form_profile.is_valid():
#             user = form.save()
#             profile = form_profile.save(commit=False)
#             profile.user = user # the user has to be saved before the profile
#             form_profile.save()

#             return render(request, 'sante.html', context)
#         else:
#             print("---ERRORS---", form.errors, form_profile.errors)
#             context['forms'] = [form, form_profile]
#             return render(request, 'compte.html', context)

#     else:
#         # GET, generate blank form
#         context['forms'] = [UserForm(),UserProfileForm()]
#     return render(request, 'compte.html', context)


# def Compte(request):
#     if request.method == "POST":
#         form = CompteForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             message.success(request, "Compte was add")
#             return HttpResponseRedirect("/")
#         else:
#             return render(request, 'compte.html', {"form":form})
       
#     else:
#         form = CompteForm()
#         return render(request, 'compte.html', {"form":form})


