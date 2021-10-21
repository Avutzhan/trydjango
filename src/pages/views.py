from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):  # python specific args
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>hello world</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):  # python specific args
    return render(request, "contact.html", {})
