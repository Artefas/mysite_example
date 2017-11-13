from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def main(request):
    text = "Hello ass hole"
    return HttpResponse(text)
