from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'courses/home.html')


def about(request):
    return render(request,'courses/about.html')

def courses(request):
    return render(request, 'courses/courses.html')