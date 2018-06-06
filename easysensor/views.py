from django.shortcuts import render
from .tasks import hello

def index(request):
    hello.delay()
    return render(request, 'easysensor/index.html')
