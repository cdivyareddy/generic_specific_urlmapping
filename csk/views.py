from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def msd(request):
    return HttpResponse('<h1>msd is a best captain</h1>')
def captain(request):
    return HttpResponse('<h1>rutuuuuuuuuuuuu is a captian of csk</h1>')