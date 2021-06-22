import django.http
from django.shortcuts import render
from rest_framework.response import Response
from django.db.models import Count
from django.db.models import Avg, Max, Min,Sum

from django.http import HttpResponse,JsonResponse
from .models import Vaccin
from .models import Vaccinateur,EffetSecondaire,Declaration,Pays,Maladie

from rest_framework import viewsets
from .serializers import VaccinSerializer
from .serializers import VaccinateurSerializer,EffetSecondaireSerializer,DeclarationSerializer,PaysSerializer,MaladieSerializer
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from django.template.loader import render_to_string  # new
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

import os







# Create your views here.
def addMaladie(request):
   vaccinateur=Vaccinateur.objects.all()
   maladie=Maladie.objects.filter(id=1)
   data = serializers.serialize('json',maladie)
   d={
      'd':data
   }
   

   return JsonResponse(data ,content_type="application/json",safe=False)
@api_view(['GET', 'POST'])
def send_email(request, format=None):
    if request.method =='POST' and request.data.get("email") :  
        val=Vaccinateur.objects.filter(email=request.data.get("email")).first()
        #return Response({'msg':val.validation})  
        if  val and val.validation:
                return Response({'msg':'email déja validé'})           
       # print(request.data.get("email"))
        email=request.data.get("email")
        text_body ="Validation de déclaration "
    
    
        html_body = render_to_string('msg/message.html',{'email': email})
        msg = EmailMultiAlternatives(subject="Test Application", from_email="djzngoApp@gmail.com",
                                to=[email], body=text_body)  

        msg.attach_alternative(html_body, "text/html")
        x=msg.send()  
        return Response({'msg':"succes",'detail':x})
    return Response({'msg':'Error'})    
@api_view(['GET'])
def validation(request):
   
    if request.method =='GET' and request.GET.get('email') :  
        email=request.GET.get('email')
        try:
         val=Vaccinateur.objects.get(email=email)
        except:
           return Response({'msg':'erreur'})  

        if  val and val.validation:
                return Response({'msg':'email déja validé'})                  
       # print(request.data.get("email"))
        val.validation=True
        val.save()
        text_body ="Declaration validé! "
    
    
        html_body = render_to_string('msg/messageValidation.html')
        msg = EmailMultiAlternatives(subject="Test Application", from_email="djangoApp@gmail.com",
                                to=[email], body=text_body)  

        msg.attach_alternative(html_body, "text/html")
        x=msg.send()  
        
        return Response({'msg':"succes",'detail':x})
    return Response({'msg':'getMethodError'})    

@api_view(['GET'])
def statVaccins(request, format=None):
   
    if request.method =='GET'  :  
   
    
        val= Vaccinateur.objects.filter(validation=True).values('vaccin','vaccin__nom').annotate(vaccount=Count('id'))
        data = list(val)
        count=Vaccinateur.objects.filter(validation=True).count()
        
        
        
       
    return Response({'msg':data,'count':count}) 

@api_view(['GET'])
def statVaccin(request, format=None):
    try:       
        vaccin=request.GET.get('vaccin')
    
   
        if request.method =='GET' and  request.GET.get('vaccin')  :  
    
            
            val= Declaration.objects.filter(vaccinateur__vaccin=vaccin,vaccinateur__validation=True).values('effetScondaire__description').annotate(vaccount=Count('vaccinateur'))
            somme=val.aggregate(somme=Sum('vaccount'))
            nom=Vaccin.objects.filter(id=vaccin).values('nom')
            stat_age=val.aggregate(moyenne_age=Avg('vaccinateur__age') ,min_age =Min('vaccinateur__age'),max_age=Max('vaccinateur__age'))
            data = list(val)
            count=Vaccinateur.objects.filter(vaccin=vaccin,validation=True).count()
            total=Vaccinateur.objects.filter(validation=True).count()

            
        
        
            return Response({'data':data,'count':count,'total':total,'stat_age':stat_age,"msg":"succes",'somme':somme['somme'],'nom':nom[0]['nom']})
    except:
        return Response({'msg':'erreur vaccin'})  
    return Response({'msg':'erreur '}) 



def index(request):
   # return HttpResponse("hello")
   vaccins= Vaccin.objects.all()
   
   return render(request, 'index.html', {'vaccins':vaccins})

class VaccinView(viewsets.ModelViewSet):
    serializer_class = VaccinSerializer
    queryset = Vaccin.objects.all()

class VaccinateurView(viewsets.ModelViewSet):
    serializer_class = VaccinateurSerializer
    queryset = Vaccinateur.objects.all()   


class EffetSecondaireView(viewsets.ModelViewSet):
    serializer_class = EffetSecondaireSerializer
    queryset = EffetSecondaire.objects.all() 


class DeclarationView(viewsets.ModelViewSet):
    serializer_class = DeclarationSerializer
    queryset = Declaration.objects.all()   

class PaysView(viewsets.ModelViewSet):
    serializer_class = PaysSerializer
    queryset = Pays.objects.all()  

class MaladieView(viewsets.ModelViewSet):
    serializer_class = MaladieSerializer
    queryset = Maladie.objects.all() 