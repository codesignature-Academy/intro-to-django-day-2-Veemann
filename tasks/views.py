from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1> Welcome to veectorian Diets website </h1>')

def contact (request):
    return HttpResponse ('<h1> Contact Veectorian Diets here</h1>')

def about (request):
    return HttpResponse('<h1> Veectorian diets is the best dietetics firm yoy can find in the world</h1>')

