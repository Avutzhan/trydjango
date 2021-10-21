from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):  # python specific args
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>hello world</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):  # python specific args
    my_context = {
        "my_text": "this is about me",
        "my_number": 123,
        "list": [123, 345, 5675]
    }

    return render(request, "contact.html", my_context)
