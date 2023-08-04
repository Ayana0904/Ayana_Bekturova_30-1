from django import forms
from products import models


class Category_create(forms.Form):
    title = forms.CharField(max_length=150)


class ProductsCreate(forms.Form):
    img = forms.ImageField(required=False)
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    prize = forms.FloatField()
    rate = forms.FloatField()
    

class ReviewCreateForm(forms.Form):
    title = forms.CharField(max_length=128)
    e_mail = forms.CharField(max_length=128)
    description = forms.CharField(widget=forms.Textarea)
    rate = forms.FloatField()
