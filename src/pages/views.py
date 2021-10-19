from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):  # python specific args
    print(args, kwargs)
    print(request.user)
    return HttpResponse("<h1>hello world</h1>")


def contact_view(request, *args, **kwargs):  # python specific args
    return HttpResponse("<h1>Contact world</h1>")
