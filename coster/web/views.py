from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from MachineLearningMF import Main

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        #get user info
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')

        info = user(id = id, pw = pw, name = name)
        info.save() #insert user info

        return redirect(index)
    else:
        form = signupForm()
        return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        #get id and pw entered
        id = request.POST.get('id')
        pw = request.POST.get('pw')

        #select and compare user info
        for u in user.objects.all():
            if(u.id == id and u.pw == pw):
                request.session['login'] = u.id
        return redirect(index)
    else:
        return HttpResponse('login fail')

def logout(request):
    del request.session['login'] #delete a login session
    return redirect('index')

def consultant(request):
    if request.method == 'POST':
        #get customer's house info
        space = request.POST.get('space')
        floor = request.POST.get('floor')
        dic = {'space': space, 'floor': floor}
        print(dic)

        result = Main.ml(space, floor) #enter into ML model
        # dic = {
        #
        # }
        return render(request, 'consultantResult.html', {'result': result})
    else:
        form = consultantForm()
        return render(request, 'consultant.html', {'form': form, 'login': request.session.get('login', 'no')})
