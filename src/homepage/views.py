from django.shortcuts import render
from homepage.models import TestModel
# Create your views here.

def home(request):
    test = TestModel.objects.get(pk=2)
    context = {
        "test": test,
    }
    return render(request, 'homepage/home.html', context)

def tinymce(request):
    return render(request, 'homepage/tinymce.html')
