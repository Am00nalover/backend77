from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request):
    context = {
        "msg": "Hello, HTML5",
        "title": "7/7 Bootcamp"
    }
    return render(request,'hello.html',context)