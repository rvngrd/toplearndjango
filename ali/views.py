from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

a = {
    '1': 'salam',
    '2': 'bye'
}


def index(request):
    return HttpResponse("salam")


def dynamic(request, id):
    return HttpResponse(f'{id} and {a.get(id)}')