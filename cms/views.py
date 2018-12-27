from django.http import HttpResponse
from django.shortcuts import redirect, reverse


def index(request):
    if request.GET.get("username"):
        return HttpResponse("这是cms首页")
    else:
        return redirect(reverse("cms:login"))


def login(request):
    return HttpResponse("这是cms登陆页面")
