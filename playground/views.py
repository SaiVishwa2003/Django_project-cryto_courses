from django.shortcuts import render

def sai(request):
    return render(request,'traing/home.html')

def reg(request):
    return render(request,'traing/register.html')
