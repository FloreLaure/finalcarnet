from django.contrib import admin
from .models import User, familiaux, vaccinal, autre, Carnet_user,UserProfile#import the Person model


# Register your models here.
admin.site.register(User)
admin.site.register(familiaux)
admin.site.register(vaccinal)
admin.site.register(autre)
admin.site.register(Carnet_user)
admin.site.register(UserProfile)



