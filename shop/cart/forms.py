
from django import forms


# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 101)]


class CartAddProductForm(forms.Form):
    # quantity = forms.TypedChoiceField(
    #                             choices=PRODUCT_QUANTITY_CHOICES,
    #                             coerce=int)
    quantity = forms.IntegerField(max_value=100, min_value=1,
        widget= forms.NumberInput(attrs={'class': 'form-control', 'id': 'quantity', 'placeholder': '0', 'value': '1', 'onfocus': "this.placeholder = ''"}))
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
