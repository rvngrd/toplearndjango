from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

a = {
    '1': 'salam',
    '2': 'bye'
}


def link(request):
    html = """
        <ul>
            <li>
                <a href="monday"> go to sunday </a>
            </li>
        </ul>
    """
    # m = render_to_string('ali/challenge.html')
    # return HttpResponse(m)
    data = [1,2,3, 'testing']
    text = 'this is a test'
    context = {
        'data': data,
        'text': text
    }
    return render(request, 'ali/challenge.html', context)


def index(request):
    return HttpResponse("salam")


def dynamic(request, id):
    m = a.get(str(id))
    if m is not None:
        return HttpResponse(f'{id} and {a.get(id)}')
    return HttpResponseNotFound("<h1> NOT FOUND </h1>")

def test_redirect(request):
    # return HttpResponseRedirect('/days/sunday')
    return HttpResponseRedirect(reverse('ali:iman'))    #if we set app_name in urls, we have to add it in reverse