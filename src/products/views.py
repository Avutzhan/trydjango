from django.shortcuts import render, get_object_or_404, redirect

from .models import Product


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


def dynamic_lookup_view(request, my_id):
    obj = Product.objects.get(id=my_id)
    context = {
        "obj": obj
    }
    return render(request, "products/product_detail.html", context)
