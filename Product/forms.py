from django import forms


class PostCreateForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(max_length=128)
    rate = forms.FloatField()
    description = forms.CharField(widget=forms.Textarea())
