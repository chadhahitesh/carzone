from django.shortcuts import render


# Create your views here.
def  home(request):
    return render (request,'pages/home.html')


def about(request):
    return render (request,'pages/about.html')

def service(request):
    return render (request,'pages/service.html')

def contactus(request):
    return render (request,'pages/contactus.html')
