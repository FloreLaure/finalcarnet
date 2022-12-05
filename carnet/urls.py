from django.urls import path 
from . import views 
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('sante/', views.sante, name='sante'),
    path('Carnet/', views.Carnet, name='Carnet'),
    path('vaccinal/', views.Voirvaccinal, name='vaccinal'),
    path('autre/', views.Voirautre, name='autre'),
    path('familiaux/', views.Voirfamiliaux, name='familiaux'),
    path('Compte/', views.Compte, name='Compte'),
    path('ajoufamiliaux/', views.antecedantFamiliaux, name='ajoufamiliaux'),
    path('ajouvaccin/', views.antecedantVaccin, name='ajouvaccin'),
    path('ajouAutre/', views.ajouAntecedant, name='ajouAutre'),
    path('login/', LoginView.as_view(
                            template_name='registration/login.html'), 
                            name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

