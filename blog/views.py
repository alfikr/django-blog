from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')


def homepage(request):
    # return HttpResponse('Home')
    return render(request, 'homepage.html')
