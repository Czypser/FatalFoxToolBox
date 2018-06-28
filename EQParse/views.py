from django.http import HttpResponse


from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the EQParse index.")
    return render(request, 'eqparseindex.html')