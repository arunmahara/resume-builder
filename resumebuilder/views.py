from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse ('<h1>hello</h1>')
    return render (request, 'index.html')