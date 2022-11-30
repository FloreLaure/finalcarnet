from django.urls import path #path function
from . import views # . is shorthand for the current directory
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
    path('sante/', views.sante, name='sante'),
    path('Carnet/', views.Carnet, name='Carnet'),

    path('vaccinal/', views.vaccinal, name='vaccinal'),
    path('autre/', views.autre, name='autre'),
    path('familiaux/', views.familiaux, name='familiaux'),
    path('Compte/', views.Compte, name='Compte'),
    path('ajoufamiliaux/', views.ajoufamiliaux, name='ajoufamiliaux'),
    path('ajouvaccin/', views.ajouvaccin, name='ajouvaccin'),
    path('ajouAutre/', views.ajouAutre, name='ajouAutre'),
   



    # --- Customized views ----
    path('login/', LoginView.as_view(
                            template_name='registration/login.html'), 
                            name='login'),# this url

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

