from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def first(request):
    return HttpResponse('Welcome to Django')
def second(request):
    return HttpResponse('Hey, I am am Rohith M P')
def third(request):
    return HttpResponse('<H1><B><U>HEY GUYS . . .</U></B></H1>')
def fourth(request):
    a='It is an MVT Pattern.'
    return HttpResponse('<H3><B><U>Django Framework</U></B></H3>'+a)

def temp1(request):
    return render(request,'HTML1.html')

def dtl(request):
    a='Hello Rohith M P.'
    return render(request,'HTML2.html',{'data':a})

def ForAndIFLoop(request):
    a='Hello Rohith M P.'
    b=[1,2,3,4,5]
    return render(request,'HTML3.html',{'data':a,'new':b})

def HTMLfour(request):
    return render(request,'HTML4.html')

def HTMLfive(request):
    return render(request,'HTML5.html')
