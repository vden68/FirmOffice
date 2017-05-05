from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(reguest):
    return HttpResponse("Hello, world. You're at the polls index.")
    #return render(reguest, 'site/home.html')
