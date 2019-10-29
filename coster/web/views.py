from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from MachineLearningMF import Main
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        #get user info
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        info = user(id = id, pw = pw, name = name, phone = phone, power = 1)
        info.save() #insert user info

        context = {
            'signup':'success'
        }

        return HttpResponse(json.dumps(context), content_type="application/json")

@csrf_exempt
def login(request):
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
            else:
                context = {
                    'login': None
                }
        return HttpResponse(json.dumps(context), content_type="application/json")

@csrf_exempt
def logout(request):
    del request.session['login'] #delete a login session
    context = {
        'login':None
    }
    return HttpResponse(json.dumps(context), content_type="application/json")

def Hub(request):
    return render(request, 'html/Hub.html')

def Intro(request):
    login = request.session.get('login', 'nologin')

    return render(request, 'html/Intro.html', {'login':login})

def consultant(request):
    if request.method == 'POST':
        # get customer's house info
        space = request.POST.get('space')
        floor = request.POST.get('floor')
        rooms = request.POST.get('rooms')
        year = request.POST.get('years')
        dong = request.POST.get('dong')
        # dong theta값 꺼내오기
        data = consulting.objects.filter(dong=dong)

        dic = {'year': year, 'rooms': rooms, 'floor': floor, 'space': space}
        print(dic)
        result = Main.ml(year, rooms, floor, space, data[0].theta0, data[0].theta1, data[0].theta2, data[0].theta3, data[0].theta4)  # enter into ML model

        return render(request, 'html/Results.html', {'result': result})
    else:
        login = request.session.get('login', 'nologin')
        return render(request, 'html/consultant.html', {'login':login})

def Results(request):
    return render(request, 'html/Results.html')

def Seller(request):
    return render(request, 'html/Seller.html')

@csrf_exempt
def si(request):
    data = request.POST.get('si')
    print(data)
    result = []
    for item in consulting.objects.filter(si = data):
        print(item.gu)
        result.append(item.gu)

    result = list(set(result)) #중복 제거
    result = json.dumps({'gu' : result}) #json 으로 변환
    return HttpResponse(result, content_type ="application/json")

@csrf_exempt
def gu(request):
    data = request.POST.get('gu')
    print(data)
    result = []
    for item in consulting.objects.filter(gu = data):
        print(item.dong)
        result.append(item.dong)

    result = list(set(result)) #중복 제거
    result = json.dumps({'dong' : result}) #json 으로 변환
    return HttpResponse(result, content_type ="application/json")

