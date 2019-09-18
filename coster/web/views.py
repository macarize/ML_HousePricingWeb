from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from MachineLearningMF import Main
import json
from django.views.decorators.csrf import csrf_exempt

def main(request):
    login = request.session.get('login')

    return render(request, 'main.html', {login: login})

def signup(request):
    if request.method == 'POST':
        #get user info
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')

        info = user(id = id, pw = pw, name = name)
        info.save() #insert user info

        return redirect(main)
    else:
        form = signupForm()
        return render(request, 'signup.html', {'form': form})

@csrf_exempt
def ajaxLogin(request):
    if request.method == 'POST':
        #get id and pw entered
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        print(id)

        #select and compare user info
        for u in user.objects.all():
            if(u.id == id and u.pw == pw):
                request.session['login'] = u.id
                print('login success')
                context = {
                    'login': request.session.get('login')
                }
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return print('login fail')

@csrf_exempt
def logout(request):
    del request.session['login'] #delete a login session
    context = {
        'login':None
    }
    return HttpResponse(json.dumps(context), content_type="application/json")

def consultant(request):
    if request.method == 'POST':
        #get customer's house info
        space = request.POST.get('space')
        floor = request.POST.get('floor')
        dic = {'space': space, 'floor': floor}
        print(dic)
        result = Main.ml(space, floor) #enter into ML model
        return render(request, 'consultantResult.html', {'result': result})
    else:
        form = consultantForm()
        return render(request, 'consultant.html', {'form': form, 'login': request.session.get('login', 'no')})
