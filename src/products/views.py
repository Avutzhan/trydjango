from django.http import Http404

from django.shortcuts import render, get_object_or_404

from .forms import ProductForm, RawProductForm

from .models import Product


def product_create_view(request):
    initial_data = {
        'title': "my title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request, my_id):
    # obj = get_object_or_404(Product, id=my_id)
    obj = Product.objects.get(id=my_id)
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404

    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)
