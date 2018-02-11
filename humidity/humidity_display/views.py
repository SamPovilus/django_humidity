from django.shortcuts import render
import datetime

from django.utils import timezone

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the humidity display index.")

def pasthours(request, hours):
    now = str(timezone.now())
    to = str(timezone.now() - datetime.timedelta(hours=hours))
    return HttpResponse(" looking from %s to %s"% (now,to))
