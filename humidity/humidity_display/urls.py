from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hours>/',views.pasthours,name='pasthours'),
]
