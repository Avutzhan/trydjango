from django.urls import path
from .views import (
    product_list_view,
    dynamic_lookup_view
)

app_name = 'products'

urlpatterns = [
    path('/', product_list_view, name="product-list"),
    path('/<int:my_id>/', dynamic_lookup_view, name="product-detail"),
]