from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price"
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "you can do it"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "you can do it",
                "class": "new-class-name two",
                "id": "my-id-for-text-area",
                "rows": 20,
                "cols": 100
            }
        )
    )
    price = forms.DecimalField(initial=199.99)
