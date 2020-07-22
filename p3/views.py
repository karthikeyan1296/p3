from django.http import HttpResponse

def index(request):
    return HttpResponse("HELLO WORLD")

def home(request):
    return HttpResponse("<h1>WELCOME TO HOME PAGE</h1>")