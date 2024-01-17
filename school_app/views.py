from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

from school_app import models   # importujeme vždy z root adresáře

import json

def hello_world(request):
    return HttpResponse("Hello, world!")

def welcome_to_school(request):
    return HttpResponse("Welcome to school!")

# chceme vrátit všechny předměty, které se nacházejí v databázi
@csrf_exempt
def list_subjects(request):
    if request.method == "GET":
        subjects = list(models.Subject.objects.values())   # vrátí list of dictionaries, které dokážeme serializovat
        return JsonResponse(subjects, safe=False, status=200)
    elif request.method == "POST":
        subject = request.body   # HTTP protokol vrátí binárku
        subject_dict = json.loads(subject)   # vrátí dictionary polí
        new_subject = models.Subject(**subject_dict) # rozbalení dictionary subject_dict
        new_subject.save()   # nový objekt se uloží do databáze
        return JsonResponse(subject_dict, status=200)
    else:
        return HttpResponseNotFound("Sorry this method is not supported")
    
@csrf_exempt
def subject_detail(request, pk):
    try:
        subject = models.Subject.objects.get(pk=pk)   # lze implementovat pomocí .filter místo .get 
    except ObjectDoesNotExist:
        return JsonResponse({"status": f"There is no subject with id {pk}"}, status=404)
    
    if request.method == "GET":
        return JsonResponse(model_to_dict(subject))
    elif request.method == "PUT":
        new_subject_bytes = request.body   # binárka
        new_subject = json.loads(new_subject_bytes)   # převedeme na dictionary
        subject.__dict__.update(new_subject)   # původní subject převeď do dictionary a uprav ho s novým dictionary, ale změň pouze ty pole, které se v něm nacházejí, zůstane _state objekt
        subject.save()
        return JsonResponse(new_subject, status=201)
    elif request.method == "DELETE":
        subject.delete()
        return HttpResponse(status=204)