from django.shortcuts import render
from django.http import HttpResponse
from . models import stud

def index(request):
    students = stud.objects.all().filter(sem="5")
    context = {'students': students}
    return render(request, 'index.html', context)

def details(request):
    return render(request, 'create.html')
