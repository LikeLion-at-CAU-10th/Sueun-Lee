from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.

def http_response(request):
    if request.method == "GET":
        return HttpResponse("Hello world!")

def json_response(request):
    if request.method == "GET":
        data = {
            'name' : 'sueun',
            'school' : 'CAU'
        }
        return JsonResponse(data=data)

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        data = {
            'name' : name
        }

        return render(request, 'index.html', context=data)
    else:
        return render(request, 'index.html')
