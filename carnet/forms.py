from django import forms
from django.forms import ModelForm, TextInput
from carnet.models import User,UserProfile,Carnet_user, familiaux, vaccinal, autre # import the models from polls/models.py
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from . import validators

def validate_nom(nom):
    # check if there are numbers in the nom
    if (nom.isalpha() == False):
        print("Invalid nom")  
        raise forms.ValidationError(f'The nom {nom} is invalid')


def validate_prenom(prenom):
    # check if there are numbers in the nom
    if (prenom.isalpha() == False):
        print("Invalid prenom")  
        raise forms.ValidationError(f'The prenom {prenom} is invalid')



## le formulaire pour la création des comptes

##  regex=r"^[\w.@+-]+$"    This value may contain only letters, numbers and "
                         # "@/./+/-/_ characters.

class CompteForm(UserCreationForm):
    username = forms.RegexField(regex=r"^[\w.@+-]+$",
        label=("Nom d'utilisateur"), max_length=20,
        help_text=("Required. 20 "),
        error_messages={
            'invalid': ("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},
        widget=forms.TextInput(attrs={'class': 'form-control',
                                'required': 'true',                         
    })
)
    password1 = forms.CharField(
        label=("Mot de passe"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'required': 'true',

        })
    )
    password2 = forms.CharField(
        label=("Confirmer le mot de passe"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'type': 'password',
                                          'required': 'true',
        }),
        help_text=("Entrer le même mot de passe")
    )

    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # exclude = ['username']
        #model = User
        fields = ['username','password1','password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),   # Remove This Line
            'password2': forms.TextInput(attrs={'class': 'form-control'}),  # Remove This Line
        }


   

class CarnetForm(forms.Form):

    class Meta:
        model = Carnet_user
        fields = '__all__' 
    



## le formulaire qui permet aux personnels soignant de renseigner les consultations et autres

class ajoutAutreForm(forms.Form):
   
    class Meta: 
        model = autre
        fields = "__all__"




## le formulaire qui permet aux personnels soignant de metre à jour les antécédants familiaux

class ajoutFamiliauxForm(forms.Form):
    class Meta():
        model = familiaux
        fields = "__all__"





class ajoutVaccinalForm(forms.Form):

    class Meta:
        model = vaccinal
        fields = "__all__"




    
class LoginUserView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        user_to_authenticate = form.cleaned_data
        print(user_to_authenticate)
        return super().form_valid(form)



class loginForm(forms.Form):
    username = forms.CharField(
        label=("Nom d'utilisateur"), max_length=20,
        error_messages={
            'invalid': ("This value may contain only letters, numbers and "
                    "@/./+/-/_ characters.")},
        widget=forms.TextInput(attrs={'class': 'form-control',
                                    'required': 'true',                         
        })
)   
    password = forms.CharField(
        label=("Mot de passe"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'required': 'true',

        })
    )



class UserForm(forms.ModelForm):
    class Meta:      
        model = User
        fields = ['username', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
        widgets = {
            'password': forms.Textarea(attrs={'class': 'password'}),
            'user': forms.CharField()
        }
