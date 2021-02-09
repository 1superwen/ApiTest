from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
def welcome(request):
    print('进来了')
    return render(request, 'welcome.html')


def home(requests):
    return render(requests, 'home.html')

