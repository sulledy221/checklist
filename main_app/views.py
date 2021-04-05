from django.shortcuts import render
from django.http import HttpResponse


def home(request):
  return HttpResponse('<h1>Hello </h1>')

# Create your views here.
def about(request):
    return render(request, 'about.html')