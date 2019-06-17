from django.shortcuts import render
from .models import *

def charts(request):
    records = Data.objects.order_by('timereg').filter(espid='Ascea')[:5000]
    return render(request, 'charts.html', {'records':records})