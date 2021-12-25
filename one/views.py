from django.shortcuts import render
# from models import *
# Create your views here.

def home(request):
    data = 20
    for homes in data:
        doll = []
        doll.append(homes)
        print(doll)

    return render(request, 'home.html')