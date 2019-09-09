from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    test = 'test'
    return render(request, 'index.html', {'test': test})

def prediction(request):
    if request.method == 'POST':
        return HttpResponse('PREDICTION RUNNING')
    else:
        return HttpResponse('PREDICTION')

def consultant(request):
    if request.method == 'POST':
        space = request.POST.get('space')
        floor = request.POST.get('floor')
        price = request.POST.get('price')
        print(space)
        dic = {'space': space, 'floor': floor, 'price': price}
        print(dic)
        return render(request, 'consultantProcessing.html', dic)
    else:
        form = consultantForm()
        return render(request, 'consultant.html', {'form': form})