from django.shortcuts import render
from .models import *

def charts(request,espid="Ascea",samples=10000):
    #records = Data.objects.order_by('timereg').filter(espid=espid)[:1000]
    url=""
    if espid=="Ascea":
        url='/records_ascea'
    else:
        url='/records_prato'
    return render(request, 'charts.html',{'url':url })#{'records':records})