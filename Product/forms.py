from django import forms
from products import models


class Category_create(forms.Form):
    title = forms.CharField(max_length=150)
    
class PostCreateForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(max_length=128)
    description = forms.CharField(widget=forms.Textarea())
    price = models.DecimalField(max_digits=10, decimal_places=2)


class ProductsCreate(forms.Form):
    img = forms.ImageField(required=False)
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    prize = forms.FloatField()
    rate = forms.FloatField()
    

class CommentsCreateForm(forms.Form):
    text = forms.CharField(max_length=300)
    name = forms.CharField(max_length=15)
