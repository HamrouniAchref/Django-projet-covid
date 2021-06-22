from django.contrib import admin
from django.urls import path , include
from . import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'vaccins', views.VaccinView, 'vaccin')
router.register(r'vaccinateur', views.VaccinateurView, 'vaccinateur')
router.register(r'effetSecondaire', views.EffetSecondaireView, 'effetSocondaure')
router.register(r'declaration', views.DeclarationView, 'declaration')
router.register(r'pays', views.PaysView, 'pays')
router.register(r'maladie', views.MaladieView, 'maladie')









urlpatterns = [
   # path('admin/', admin.site.urls)
    path('',views.index,name='index'),
    path('api/', include(router.urls)),
    path('api/addMaladie', views.addMaladie, name='addMaladie'),
    path('mal/', views.send_email),
    path('validation/', views.validation),
    path('api/statVaccins', views.statVaccins),
    path('api/statVaccin', views.statVaccin),


]