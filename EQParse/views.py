from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the EQParse index.")
    # loader.get_template('EQParse/eqparse.html')
    # return HttpResponse('')
    
    return render(request, 'eqparse.html')