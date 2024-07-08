from django.http import HttpResponse
from django.template import loader

from . import layout

def index(request):
    template = loader.get_template('index.html')
    context = {
        'n':0,
    }
    return HttpResponse(template.render(context, request))
