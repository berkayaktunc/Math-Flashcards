from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def subtract(request):
    return render(request, 'subtract.html', {})


def add(request):
    return render(request, 'add.html', {})


def multiple(request):
    return render(request, 'multiple.html', {})


def divide(request):
    return render(request, 'divide.html', {})
