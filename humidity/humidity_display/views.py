from django.shortcuts import render
import datetime

from django.utils import timezone
from .models import Humidity
# Create your views here.
from django.http import HttpResponse


def index(request):
    humidities = Humidity.objects.order_by('-log_date')[:5]
    context = {'humidities': humidities}
    return render(request, 'humidity_display/index.html', context)

def pasthours(request, hours):
    now = str(timezone.now())
    to = str(timezone.now() - datetime.timedelta(hours=hours))
    return HttpResponse(" looking from %s to %s"% (now,to))
