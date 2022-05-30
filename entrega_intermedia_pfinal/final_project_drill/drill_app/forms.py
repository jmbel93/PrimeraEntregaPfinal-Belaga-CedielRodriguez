from django import forms
from django.forms import ModelForm


class RentABookForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Name of the book')
    rented_date = forms.DateField(
        label='Rented Date',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )

class BuyABookForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Name of the book')
    amount = forms.IntegerField(label='Amount to buy')

class SellABookForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Name of the book')
    genre = forms.CharField(max_length=40, min_length=3, label='Genre of the book')
    amount = forms.IntegerField(label='Amount to sell')