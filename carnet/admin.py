from django.contrib import admin
from .models import User, familiaux,UserProfil, vaccinal, autre,carnetUser#import the Person model


# Register your models here.
admin.site.register(User)
admin.site.register(familiaux)
admin.site.register(vaccinal)
admin.site.register(autre)
admin.site.register(carnetUser)
admin.site.register(UserProfil
)




