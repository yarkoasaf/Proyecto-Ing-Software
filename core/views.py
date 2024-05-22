from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def registro(request):
    return render (request, 'registration/registro.html')
# Create your views here.
