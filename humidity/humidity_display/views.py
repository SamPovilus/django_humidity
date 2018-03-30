from django.shortcuts import render, render_to_response
import datetime
import time
from django.utils import timezone
from .models import Humidity
from .models import Pressure
# Create your views here.
from django.http import HttpResponse
from chartit import DataPool, Chart

def index(request):
    humidities = Humidity.objects.order_by('-log_date')[:200]
    context = {'humidities': humidities}
    return render(request, 'humidity_display/index.html', context)

def pressure_list(request):
    pressures = Pressure.objects.order_by('-log_date')[:200]
    context = {'pressures': pressures}
    return render(request, 'humidity_display/pressure_list.html', context)

def pasthours(request, hours):
    now = str(timezone.now())
    to = str(timezone.now() - datetime.timedelta(hours=hours))
    return HttpResponse(" looking from %s to %s"% (now,to))

def chart(request):
    hdata =  Humidity.objects.filter()#humidity__gt=0)
    #hdata = hdata[:50]
    humiditydata = \
                   DataPool(
                       series =
                       [{'options' : {
                           'source': hdata},
                         'terms': [
                             'humidity',
                             'temp',
                             #('log_date', lambda d: time.mktime(d.timetuple())),
                             'log_date'
                         ]
                         }
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
                 'text': "Time"}}},
#    x_sortf_mapf_mts=(None, lambda i: datetime.datetime.fromtimestamp(i).strftime("%H:%M"), False)
    )
    return render_to_response('humidity_display/chart.html',{'humiditychart':cht})

                  
