from django.shortcuts import render
from django.http import HttpResponse
from main.models import Score


def home(request):
    return HttpResponse('<h1>Welcome</h1>')


def data(request):
    context = {
        'scores': Score.objects.all()
    }
    return render(request, 'main/data.html', context)