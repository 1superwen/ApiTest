from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
def welcome(request):
    print('进来了')
    return render(request, 'welcome.html')

# 返回子页面
def child(request, eid, oid):
    return render(request, eid)



def home(request):
    return render(request, 'welcome.html', {"whichHTML": "Home.html", "oid": ""})

