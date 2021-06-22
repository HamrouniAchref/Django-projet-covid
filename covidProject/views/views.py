from django.http import HttpResponse
from django.shortcuts import render 
import requests
from django.core.mail import send_mail




def home(request):
# r=requests.get('https://api.covid19api.com/live/country/tunisia/status/confirmed/date/2020-03-21T13:13:30Z')
 
 return HttpResponse("r.text,content_type='application/json'")
    