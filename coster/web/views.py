from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from MachineLearningMF import Main

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')

        info = user(id = id, pw = pw, name = name)
        info.save()

        return redirect(index)
    else:
        form = signupForm()
        return render(request, 'signup.html', {'form': form})

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
        dic = {'space': space, 'floor': floor}
        print(dic)

        result = mlTest.ml(space, floor)
        return render(request, 'consultantProcessing.html', {'result': result})
    else:
        form = consultantForm()
        return render(request, 'consultant.html', {'form': form})