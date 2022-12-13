from django.contrib import admin
from .models import familiaux,UserProfil, vaccinal, ajouAutre,carnetUser#import the Person model


# Register your models here.
admin.site.register(familiaux)
admin.site.register(vaccinal)
admin.site.register(ajouAutre)
admin.site.register(carnetUser)
admin.site.register(UserProfil
)




