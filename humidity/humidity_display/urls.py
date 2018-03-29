from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hours>/',views.pasthours,name='pasthours'),
    path('chart/',views.chart,name='chart'),
    path('pressures/',views.pressure_list,name='pressure'),
]
