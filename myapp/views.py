from django.http import HttpResponse
from .forms import AddPostForm
from django.shortcuts import render
# Create your views here.

def about(request):
    return HttpResponse('<h1>About site</h1>')

def login(request):
    return HttpResponse('<h1>Page login</h1>')

def contacts(request, id):
    url_id = id
    name = request.GET.get('name')
    age = request.GET.get('age')
    get_params = {'name': name, 'age': age}
    return HttpResponse(f'Page contacts, url_parametr_id = {url_id}, get_params - {get_params}')

def add_form(request):
    form = AddPostForm()
    return render(request, 'myapp/addform.html', {'form': form})

def index(request):
    return HttpResponse('<h1>Main page</h1>')

def index_myapp(request):
    return HttpResponse('<h1>MyApp page</h1>')