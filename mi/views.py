from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rohith(request):
    return HttpResponse('<h1>he is an hitman<h1>')
def captain(request):
    return HttpResponse('<h1>hardhik is a mi captain<h1>')