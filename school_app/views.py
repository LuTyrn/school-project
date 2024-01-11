from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world!")

def welcome_to_school(request):
    return HttpResponse("Welcome to school!")
