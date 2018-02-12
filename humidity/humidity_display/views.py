from django.shortcuts import render, render_to_response
import datetime

from django.utils import timezone
from .models import Humidity
# Create your views here.
from django.http import HttpResponse
from chartit import DataPool, Chart

def index(request):
    humidities = Humidity.objects.order_by('-log_date')[:200]
    context = {'humidities': humidities}
    return render(request, 'humidity_display/index.html', context)

def pasthours(request, hours):
    now = str(timezone.now())
    to = str(timezone.now() - datetime.timedelta(hours=hours))
    return HttpResponse(" looking from %s to %s"% (now,to))

def chart(request):
    hdata =  Humidity.objects.filter(log_date__second__lt=1)
    humiditydata = \
                   DataPool(
                       series =
                       [{'options' : {
                           'source': hdata},
                         'terms': [
                             'humidity',
                             'temp',
                             'log_date']}
                        ])
    cht = Chart(
        datasource = humiditydata,
        series_options =
        [{'options':{
            'type' : 'line',
            'stacking' : False},
          'terms':{
              'log_date':[
                  'humidity',
                  'temp']
              }}],
        chart_options =
        {'title':{
            'text':"Humidity and Temp data for my apartment"},
         'xAxis':{
             'title' :{
                 'text': "Time"}}})
    #return render(request, 'humidity_display/chart.html', cht)

    return render_to_response('humidity_display/chart.html',{'humiditychart':cht})

                  
