from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

a = {
    '1': 'salam',
    '2': 'bye'
}


def index(request):
    return HttpResponse("salam")


def dynamic(request, id):
    m = a.get(id)
    if m is not None:
        return HttpResponse(f'{id} and {a.get(id)}')
    
    return HttpResponseNotFound("NOT FOUND")

def test_redirect(request):
    return HttpResponseRedirect('/days/sunday')