from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . import graphing

def index(request):
    template = loader.get_template('index.html')
    context = {
        'fruits': ['apple', 'banana', 'cherry'],
    }
    return HttpResponse(template.render(context, request))
