from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    test = 'test'
    return render(request, 'index.html', {'test': test})

def login(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        for u in user.objects.all():
            if(u.id == id and u.pw == pw):
                request.session['login'] = u.id
        return redirect(index)
    else:
        return HttpResponse('login fail')

def logout(request):
    del request.session['login']
    return redirect('index')

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