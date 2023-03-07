from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def chandana(request):
    return HttpResponse("<marquee><h1>I am Chandana Kamalapuram......!</h1></marquee>")


def prem(request):
    return HttpResponse("<marquee><h1>Divya laptop is not working.....</h1></marquee>")