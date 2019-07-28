from django.shortcuts import render
from .serializers import LaptopSerializer
from .models import Laptop
from rest_framework import viewsets


# Create your views here.
class LaptopViewSet(viewsets.ModelViewSet):
    serializer_class = LaptopSerializer
    queryset = Laptop.objects.all()
    # queryset = LaptopSerializer.objects.all()

from django.http import HttpResponse

def aaa(request):
    print(request.__dict__)
    return HttpResponse('<h1>request</h1>')
