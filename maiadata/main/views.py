from django.shortcuts import render
from .models import *

def charts(request,espid="Ascea",samples=10000):
    records = Data.objects.order_by('timereg').filter(espid=espid)[:1000]
    return render(request, 'charts.html', {'records':records})