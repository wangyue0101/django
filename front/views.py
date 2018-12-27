from django.http import HttpResponse
from django.shortcuts import redirect, reverse, render
from django.template.loader import render_to_string


# def index(request):
#     html = render_to_string("index.html")
#     return HttpResponse(html)

def index(request):
    return render(request, "index.html")