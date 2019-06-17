from django.shortcuts import render
from .models import *

def charts(request,espid="Ascea"):
    records = Data.objects.order_by('timereg').filter(espid=espid)
    return render(request, 'charts.html', {'records':records})