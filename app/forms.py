from django import forms

class ImageForm(forms.Form):
    profile_pic = forms.ImageField()
    caption = forms.CharField(max_length=300)