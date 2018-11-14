from django.shortcuts import render,redirect
from django.http import HttpResponse

i = None
j = None
def input(request):
    return render(request,'add.html')
def output(request):
    val1 = request.GET['t1']
    val2 = request.GET['t2']
    global i
    global j
    i = int(val1)
    j = int(val2)
    z = request.GET['but']
    if z == 'add':
        return redirect(add)
    if z == 'sub':
        return redirect(sub)
    if z == 'mul':
        return redirect(mul)
    if z == 'div':
        return redirect(div)
    if z == 'floor':
        return redirect(floor)
    if z == 'mod':
        return redirect('/mod')
def add(request):
    k = i+j
    data = 'The addition of ',i,'  and  ',j,'  is:  ',k
    return HttpResponse(data)
def sub(request):
    k = i-j
    data = 'The substraction of  ',i,'  and  ',j,'  is:  ',k
    return HttpResponse(data)
def mul(request):
    k = i*j
    data = 'The multiplication of  ',i,'  and  ',j,'  is:  ',k
    return HttpResponse(data)
def div(request):
    k = i/j
    data = 'The division of  ',i,'  and  ',j,'  is:  ',k
    return HttpResponse(data)
def floor(request):
    k = i//j
    data = 'The floor division of  ',i,'  and  ',j,'  is:  ',k
    return HttpResponse(data)
def mod(request):
    k = i%j
    data = 'The modulus of  ',i,'  and  ',j,'  is:  ',k
    return HttpResponse(data)

